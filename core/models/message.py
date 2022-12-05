from django.db import models

from core.models.member import Member


class Message(models.Model):
    messageContent = models.CharField(max_length=50, null=False, blank=False)
    messageFileUrl = models.FileField(verbose_name="CSV File", upload_to='message_files/', blank=True, null=True)
    memberFrom = models.ForeignKey(Member, related_name="memberFrom", on_delete=models.CASCADE)
    memberTo = models.ForeignKey(Member, related_name="memberTo", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
