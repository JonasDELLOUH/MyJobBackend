from django.db import models


class Member(models.Model):
    token = models.CharField(max_length=3000, null=True, blank=True)
    email = models.EmailField("email address", blank=True)
    photoUrl = models.ImageField(verbose_name="CSV File", upload_to='csv_files', blank=True, null=True)
    displayName = models.CharField(max_length=50, null=False, blank=False)
    phoneNumber = models.CharField(max_length=50, null=True, blank=True)
    aboutMe = models.CharField(max_length=300, null=True, blank=False)
    isWorker = models.BooleanField(verbose_name="IsWorker", auto_created=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.displayName
