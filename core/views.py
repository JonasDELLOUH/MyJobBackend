# Create your views here.
from requests import Response
from rest_framework.viewsets import ModelViewSet

from core.models.address import Address
from core.models.job import Job
from core.models.job_category import JobCategory
from core.models.member import Member
from core.models.message import Message
from core.models.post import Post
from core.models.post_comment import PostComment
from core.models.post_like import PostLike
from core.models.worker import Worker
from core.models.workshop import Workshop
from core.serializers.adress_serializer import AddressSerializer
from core.serializers.job_category_serializer import JobCategorySerializer
from core.serializers.job_serializer import JobSerializer
from core.serializers.member_serializer import MemberSerializer
from core.serializers.message_serializer import MessageSerializer
from core.serializers.post_comment_serializer import PostCommentSerializer
from core.serializers.post_like_serializer import PostLikeSerializer
from core.serializers.post_serializer import PostSerializer
from core.serializers.worker_serializer import WorkerSerializer
from core.serializers.workshop_serializer import WorkshopSerializer


class MemberViewSet(ModelViewSet):
    permission_classes = []
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PostViewSet(ModelViewSet):
    permission_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     post = Post.objects.all()
    #     return post
    #
    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #
    #     new_post = Post.objects.create(worker=Worker.objects.filter(id=data["worker_id"])[0],
    #                                    postText=data["postText"], )
    #     print(data["postcomments_ids"])
    #     print("aaaaaaaaaaaaaaa")
    #     if data["postcomments_ids"]:
    #         for postcomment_id in data["postcomments_ids"]:
    #             postcomment_obj = PostComment.objects.get(id=postcomment_id)
    #             new_post.postcomments.add(postcomment_obj)
    #     if data["postlikes_ids"]:
    #         for postlike_id in data["postlikes_ids"]:
    #             postlike_obj = PostLike.objects.get(id=postlike_id)
    #             new_post.postlikes.add(postlike_obj)
    #
    #     serializer = PostSerializer(new_post)
    #
    #     return Response(serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = PostSerializer(instance=instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     instance.save
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # # def update(self, request, *args, **kwargs):
    # #     data = request.data
    # #     instance = self.get_object()
    # #     if data["postcomments_ids"]:
    # #         for postcomment_id in data["postcomments_ids"]:
    # #             postcomment_obj = PostComment.objects.get(id=postcomment_id)
    # #             instance.postcomments.set(postcomment_obj)
    # #     if data["postlikes_ids"]:
    # #         for postlike_id in data["postlikes_ids"]:
    # #             postlike_obj = PostLike.objects.get(id=postlike_id)
    # #             instance.postlikes.set(postlike_obj)
    # #     if data["postText"]:
    # #         instance.postText = data["postText"]
    # #     if data["worker_id"]:
    # #         worker_obj = Worker.objects.get(id=data["worker_id"])
    # #         instance.worker = worker_obj
    # #
    # #     if data["postContentUrl"]:
    # #         instance.postContentUrl = data.postContentUrl
    # #
    # #     instance.save
    # #     serializer = self.get_serializer(data)
    # #
    # #     return Response(serializer.data)


class PostCommentViewSet(ModelViewSet):
    permission_classes = []
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer


class PostLikeViewSet(ModelViewSet):
    permission_classes = []
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class JobViewSet(ModelViewSet):
    permission_classes = []
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobCategoryViewSet(ModelViewSet):
    permission_classes = []
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class AddressViewSet(ModelViewSet):
    permission_classes = []
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class WorkshopViewSet(ModelViewSet):
    permission_classes = []
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class WorkerViewSet(ModelViewSet):
    permission_classes = []
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class MessageViewSet(ModelViewSet):
    permission_classes = ()
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        member_to_id = self.request.query_params.get('member_to')
        member_from_id = self.request.query_params.get('member_from')

        member_to = Member.objects.filter(id=member_to_id).first()
        member_from = Member.objects.filter(id=member_from_id).first()

        queryset = Message.objects.filter(memberFrom=member_from, memberTo=member_to)

        return queryset


class DiscussionViewSet(ModelViewSet):
    permission_classes = ()
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        member_id = self.request.query_params.get('member')
        member = Member.objects.filter(id=member_id).first()

        queryset1 = Message.objects.filter(memberFrom=member)
        queryset2 = Message.objects.filter(memberTo=member)
        myList = []
        for o in queryset1:
            myList.append(o)
        for o in queryset2:
            myList.append(o)

        queryset = myList
        # queryset.sort()

        return queryset
