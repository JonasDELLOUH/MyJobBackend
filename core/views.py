# Create your views here.
import operator

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


class PostWithCatViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        job_category_id = self.request.query_params.get('job_category')
        job_category = JobCategory.objects.filter(id=job_category_id)

        job = Job.objects.filter(jobCategory=job_category).first()
        worker = Worker.objects.filter(job=job)

        queryset = Post.objects.filter(worker=worker)
        return queryset


class PostOfWorkerViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        worker_id = self.request.query_params.get('worker')
        worker = Worker.objects.filter(id=worker_id).first()

        queryset = Post.objects.filter(worker=worker)
        return queryset


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
    # queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self):
        if self.request.query_params.get('name'):
            name = self.request.query_params.get('name')
            members = Member.objects.filter(displayName__regex=r'^' + name + '*')
            workers = []
            for member in members:
                worker = Worker.objects.filter(member=member).first()
                workers.append(worker)

            queryset = workers
            return queryset
        if self.request.query_params.get('job_name'):
            job_name = self.request.query_params.get('job_name')
            jobs = Job.objects.filter(jobName__regex=r'^' + job_name + '*')
            workers = []
            for job in jobs:
                worker = Worker.objects.filter(job=job).first()
                workers.append(worker)
            queryset = workers
            return queryset
        if self.request.query_params.get('job_category_name'):
            job_category_name = self.request.query_params.get('job_category_name')
            job_categories = JobCategory.objects.filter(jobCategoryName__regex=r'^' + job_category_name + '*')
            workers = []
            for job_category in job_categories:
                job = Job.objects.filter(jobCategory=job_category).first()
                worker = Worker.objects.filter(job=job).first()
                workers.append(worker)
            queryset = workers
            return queryset

        return Worker.objects


class MessageViewSet(ModelViewSet):
    permission_classes = ()
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        member_to_id = self.request.query_params.get('member_to')
        member_from_id = self.request.query_params.get('member_from')

        member_to = Member.objects.filter(id=member_to_id).first()
        member_from = Member.objects.filter(id=member_from_id).first()

        queryset1 = Message.objects.filter(memberFrom=member_from, memberTo=member_to)
        queryset2 = Message.objects.filter(memberFrom=member_to, memberTo=member_from)

        myList = []
        for o in queryset1:
            myList.append(o)
        for o in queryset2:
            myList.append(o)

        myList.sort(key=operator.attrgetter("date_created"))

        queryset = myList

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
        messages = []
        for o in queryset1:
            messages.append(o)
        for o in queryset2:
            messages.append(o)
        messages.sort(key=operator.attrgetter("date_created"), reverse=True)
        i = 0
        while i < len(messages):
            j = i + 1
            while j < len(messages):
                if ((messages[i].memberTo.id == messages[j].memberTo.id and messages[i].memberFrom.id == messages[
                    j].memberFrom.id)
                        or (messages[i].memberTo.id == messages[j].memberFrom.id and messages[i].memberFrom.id ==
                            messages[
                                j].memberTo.id)):
                    print("yesss remove")
                    messages.pop(j)
                    j -= 1
                j += 1
            i += 1
        queryset = messages

        return queryset
