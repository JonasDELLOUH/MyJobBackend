from django.db import models

from core.models.job_category import JobCategory


class Job(models.Model):
    jobName = models.CharField(max_length=50, null=False, blank=False)
    jobImageUrl = models.FileField(verbose_name="CSV File", upload_to='csv_files', blank=True, null=True)
    jobCategory = models.ForeignKey(JobCategory, related_name="jobCategory", on_delete=models.CASCADE, null=False)
