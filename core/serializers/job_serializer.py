from rest_framework import serializers

from core.models.job import Job
from core.models.job_category import JobCategory
from core.serializers.job_category_serializer import JobCategorySerializer


class JobSerializer(serializers.ModelSerializer):
    jobCategory = JobCategorySerializer(required=False, read_only=True)
    jobCategory_id = serializers.PrimaryKeyRelatedField(write_only=True, source='jobCategory',
                                                        queryset=JobCategory.objects.all())

    # yess
    class Meta:
        model = Job
        fields = [
            'id',
            'jobName',
            'jobImageUrl',
            'jobCategory',
            'jobCategory_id'
        ]
