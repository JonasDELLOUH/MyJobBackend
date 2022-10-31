from rest_framework import serializers

from core.models.job import Job
from core.models.job_category import JobCategory
from core.serializers.job_category_serializer import JobCategorySerializer


class JobSerializer(serializers.ModelSerializer):
    jobCategory = JobCategorySerializer(required=False, read_only=True)
    jobCategory_id = serializers.PrimaryKeyRelatedField(write_only=True, source='member',
                                                        queryset=JobCategory.objects.all())

    class Meta:
        model = Job
        fields = '__all__'
