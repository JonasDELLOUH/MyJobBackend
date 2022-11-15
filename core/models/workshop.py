from django.db import models

from core.models.address import Address


class Workshop(models.Model):
    workshopName = models.CharField(max_length=50, null=False, blank=False)
    workshopImageUrl = models.FileField(verbose_name="CSV File", upload_to='csv_files', blank=True, null=True)
    address = models.ForeignKey(Address, related_name="address", on_delete=models.CASCADE, null=False)
