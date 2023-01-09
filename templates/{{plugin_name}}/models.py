from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

class {{class_name}}(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    default_action = models.CharField(
        max_length=30
    )
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name