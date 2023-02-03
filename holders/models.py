from django.db import models

from core.models import AuditableEntity


# Create your models here.
class HolderGroup(AuditableEntity):
    label = models.CharField("label", max_length=36, blank=False, null=False)
    holder = models.ForeignKey(
        "Holder", null=True, blank=True, on_delete=models.CASCADE
    )
    readers = models.ManyToManyField("libraries.Reader")


class Holder(AuditableEntity):
    class HolderType(models.TextChoices):
        ASSOCIATION = "AS", "Association"
        SCHOOL = "SC", "School"
        CITY = "CT", "City"
        COMPANY = "CP", "Company"

    type = models.CharField(
        max_length=2, choices=HolderType.choices, default=HolderType.SCHOOL
    )
    name = models.CharField("name", max_length=24, null=False, blank=False)
