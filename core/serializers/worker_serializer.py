from rest_framework import serializers

from core.models.job import Job
from core.models.member import Member
from core.models.worker import Worker
from core.models.workshop import Workshop
from core.serializers.job_serializer import JobSerializer
from core.serializers.member_serializer import MemberSerializer
from core.serializers.workshop_serializer import WorkshopSerializer


class WorkerSerializer(serializers.ModelSerializer):
    member = MemberSerializer(required=False, read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(write_only=True, source='member', queryset=Member.objects.all())
    workshop = WorkshopSerializer(required=False, read_only=True)
    workshop_id = serializers.PrimaryKeyRelatedField(write_only=True, source='workshop',
                                                     queryset=Workshop.objects.all())
    job = JobSerializer(required=False, read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(write_only=True, source='job',
                                                queryset=Job.objects.all())

    class Meta:
        model = Worker
        fields = [
            'id',
            'member',
            'member_id',
            'workshop',
            'workshop_id',
            'job',
            'job_id'
        ]
