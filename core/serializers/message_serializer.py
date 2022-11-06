from rest_framework import serializers

from core.models.member import Member
from core.models.message import Message
from core.serializers.member_serializer import MemberSerializer


class MessageSerializer(serializers.ModelSerializer):
    memberTo = MemberSerializer(required=False, read_only=True)
    memberTo_id = serializers.PrimaryKeyRelatedField(write_only=True, source='memberTo', queryset=Member.objects.all())
    memberFrom = MemberSerializer(required=False, read_only=True)
    memberFrom_id = serializers.PrimaryKeyRelatedField(write_only=True, source='memberFrom',
                                                       queryset=Member.objects.all())

    class Meta:
        model = Message
        fields = [
            'messageContent',
            'messageFileUrl',
            'memberFrom',
            'memberFrom_id',
            'memberTo',
            'memberTo_id',
            'date_created'
        ]
