from rest_framework import serializers

from core.models.member import Member
from core.models.post_comment import PostComment
from core.serializers.member_serializer import MemberSerializer


class PostCommentSerializer(serializers.ModelSerializer):
    member = MemberSerializer(required=False, read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(write_only=True, source='member', queryset=Member.objects.all())

    class Meta:
        model = PostComment
        fields = [
            'member',
            'member_id',
            'postCommentText',
            'date_created',
            'date_updated'
        ]
