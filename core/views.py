from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework.viewsets import ModelViewSet

from core.models.job import Job
from core.models.job_category import JobCategory
from core.models.member import Member
from core.models.post import Post
from core.models.post_comment import PostComment
from core.models.post_like import PostLike
from core.serializers.job_category_serializer import JobCategorySerializer
from core.serializers.job_serializer import JobSerializer
from core.serializers.member_serializer import MemberSerializer
from core.serializers.post_comment_serializer import PostCommentSerializer
from core.serializers.post_like_serializer import PostLikeSerializer
from core.serializers.post_serializer import PostSerializer


class MemberViewSet(ModelViewSet):
    permission_classes = []
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PostViewSet(ModelViewSet):
    permission_classes = []
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.all()
        return post

    def create(self, request, *args, **kwargs):
        data = request.data

        new_post = Post.objects.create(member=Member.objects.filter(id=data["member_id"])[0],
                                       postText=data["postText"], )

        for postcomment_id in data["postcomments_ids"]:
            postcomment_obj = PostComment.objects.get(id=postcomment_id)
            new_post.postcomments.add(postcomment_obj)

        for postlike_id in data["postlikes_ids"]:
            postlike_obj = PostLike.objects.get(id=postlike_id)
            new_post.postlikes.add(postlike_obj)

        serializer = PostSerializer(new_post)

        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = PostSerializer(instance=instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


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
