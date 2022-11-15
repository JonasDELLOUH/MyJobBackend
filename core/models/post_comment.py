from django.db import models

from core.models.member import Member


class PostComment(models.Model):
    member = models.ForeignKey(Member, related_name="postCommentMember", on_delete=models.CASCADE)
    postCommentText = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
