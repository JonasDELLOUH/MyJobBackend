from rest_framework import serializers

from core.models.member import Member
from core.models.post_like import PostLike
from core.serializers.member_serializer import MemberSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    member = MemberSerializer(required=False, read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(write_only=True, source='member', queryset=Member.objects.all())

    class Meta:
        model = PostLike
        fields = [
            'id',
            'member',
            'member_id',
            'date_created'
        ]
