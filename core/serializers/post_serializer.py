from rest_framework import serializers

from core.models.member import Member
from core.models.post import Post
from core.models.post_comment import PostComment
from core.models.post_like import PostLike
from core.serializers.member_serializer import MemberSerializer
from core.serializers.post_comment_serializer import PostCommentSerializer
from core.serializers.post_like_serializer import PostLikeSerializer


class PostSerializer(serializers.ModelSerializer):
    member = MemberSerializer(required=False, read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(write_only=True, source='member', queryset=Member.objects.all())

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

    def create(self, validated_data, post):
        postcomments_data = validated_data.pop('post_comments')
        postlikes_data = validated_data.pop('postlikes_data')
        post = Post.objects.create(**validated_data)
        for postcomment_data in postcomments_data:
            Post.objects.create(post=post, **postcomment_data)

        for postlike_data in postlikes_data:
            Post.objects.create(post=post, **postlike_data)

        return post

    # def update(self, post, validated_data):
    #     post.postText = validated_data.get('postText', post.postText)
    #
    #     postcomments_data = validated_data.get('post_comments')
    #     if postcomments_data:
    #         post.post_comments_set.clear()
    #         for post_comment_data in postcomments_data:
    #             Post.objects.create(post=post, **post_comment_data)
    #
    #     postlikes_data = validated_data.get('postlikes')
    #     if postlikes_data:
    #         for postlike_data in postlikes_data:
    #             Post.objects.create(post=post, **postlike_data)
    #     post.save()
    #     return post

    def update(self, instance, validated_data):
        instance.postText = validated_data.get('postText', instance.postText)
        instance.postContentUrl = validated_data.get('postContentUrl', instance.postContentUrl)

        if 'postcomments' in validated_data:  # to handle PATCH request
            instance.postcomments.set(validated_data['postcomments'])

        if 'postlikes' in validated_data:  # to handle PATCH request
            instance.postlikes.set(validated_data['postlikes'])
        return instance

    class Meta:
        model = Post
        fields = [
            'id',
            'member',
            'member_id',
            'postText',
            'postContentUrl',
            'date_created',
            'date_updated',
            'postcomments',
            'postlikes',
            'postcomments_ids',
            'postlikes_ids'
        ]
