from django.db import models


class JobCategory(models.Model):
    jobCategoryName = models.CharField(max_length=50, null=False, blank=False)
    jobCategoryImageUrl = models.FileField(verbose_name="CSV File", upload_to='job_category_images/', blank=True, null=True)
