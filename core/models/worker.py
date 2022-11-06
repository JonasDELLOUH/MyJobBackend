from django.db import models

from core.models.job import Job
from core.models.member import Member
from core.models.workshop import Workshop


class Worker(models.Model):
    member = models.ForeignKey(Member, related_name="workerMember", on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, related_name="workshop", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="job", on_delete=models.CASCADE)
