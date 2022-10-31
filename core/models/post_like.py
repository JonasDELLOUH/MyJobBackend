from django.db import models

from core.models.member import Member


class PostLike(models.Model):
    member = models.ForeignKey(Member, related_name="member", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
