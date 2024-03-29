from rest_framework import serializers

from core.models.member import Member
from core.models.post import Post
from core.models.post_comment import PostComment
from core.models.post_like import PostLike
from core.models.worker import Worker
from core.serializers.post_comment_serializer import PostCommentSerializer
from core.serializers.post_like_serializer import PostLikeSerializer
from core.serializers.worker_serializer import WorkerSerializer


class PostSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(required=False, read_only=True)
    worker_id = serializers.PrimaryKeyRelatedField(write_only=True, source='worker', queryset=Worker.objects.all())

    postlikes = PostLikeSerializer(many=True, required=False, read_only=True)
    postlikes_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        source='postlikes',  # just to make it looks a little bit better
        queryset=PostLike.objects.all()
    )

    postcomments = PostCommentSerializer(many=True, required=False, read_only=True)
    postcomments_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        source='postcomments',  # just to make it looks a little bit better
        queryset=PostComment.objects.all()
    )

    # def create(self, validated_data, post):
    #     # postworker_data = validated_data.pop('worker')
    #     postcomments_data = validated_data.pop('post_comments')
    #     postlikes_data = validated_data.pop('postlikes_data')
    #     post = Post.objects.create(**validated_data)
    #     for postcomment_data in postcomments_data:
    #         Post.objects.create(post=post, **postcomment_data)
    #
    #     for postlike_data in postlikes_data:
    #         Post.objects.create(post=post, **postlike_data)
    #
    #     # Post.objects.create(post=post, **postworker_data)
    #
    #     return post
    #
    # # def update(self, post, validated_data):
    # #     post.postText = validated_data.get('postText', post.postText)
    # #
    # #     postcomments_data = validated_data.get('post_comments')
    # #     if postcomments_data:
    # #         post.post_comments_set.clear()
    # #         for post_comment_data in postcomments_data:
    # #             Post.objects.create(post=post, **post_comment_data)
    # #
    # #     postlikes_data = validated_data.get('postlikes')
    # #     if postlikes_data:
    # #         for postlike_data in postlikes_data:
    # #             Post.objects.create(post=post, **postlike_data)
    # #     post.save()
    # #     return post
    #
    # def update(self, instance, validated_data):
    #     instance.postText = validated_data.get('postText', instance.postText)
    #     instance.postContentUrl = validated_data.get('postContentUrl', instance.postContentUrl)
    #     # instance.worker = validated_data.get('worker', instance.worker)
    #
    #     if 'postcomments' in validated_data:  # to handle PATCH request
    #         instance.postcomments.set(validated_data['postcomments'])
    #
    #     if 'postlikes' in validated_data:  # to handle PATCH request
    #         instance.postlikes.set(validated_data['postlikes'])
    #
    #     if 'worker' in validated_data:
    #         instance.worker = validated_data['worker']
    #
    #     if 'postText' in validated_data:
    #         instance.postText = validated_data['postText']
    #
    #     if 'postContentUrl' in validated_data:
    #         instance.postContentUrl = validated_data['postContentUrl']
    #
    #     # if 'worker' in validated_data:
    #     #     instance.worker.set(validated_data['worker'])
    #
    #     instance.save
    #
    #     return instance

    class Meta:
        model = Post
        fields = [
            'id',
            'worker',
            'worker_id',
            'postText',
            'postContentUrl',
            'date_created',
            'date_updated',
            'postcomments',
            'postlikes',
            'postcomments_ids',
            'postlikes_ids'
        ]
