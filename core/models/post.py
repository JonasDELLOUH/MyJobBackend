from django.db import models

from core.models.member import Member
from core.models.post_comment import PostComment
from core.models.post_like import PostLike


class Post(models.Model):
    worker = models.ForeignKey(Member, related_name="worker", on_delete=models.CASCADE, null=False)
    postText = models.TextField(blank=True, null=True)
    postContentUrl = models.FileField(verbose_name="CSV File", upload_to='csv_files', blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    postcomments = models.ManyToManyField(PostComment, related_name="postComments",
                                          blank=True)
    postlikes = models.ManyToManyField(PostLike, related_name="postLikes",
                                       blank=True)
