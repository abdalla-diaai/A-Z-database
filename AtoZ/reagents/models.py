from django.contrib.auth.models import AbstractUser
from django import forms
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Reagent(TimeStampedModel):
    created = TimeStampedModel.created_at
    reagent_name = models.CharField(max_length=300)
    catalogue_no = models.CharField(max_length=300)
    catalogue_url = models.CharField(max_length=300)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    reagent_storage = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"{self.owner} {self.reagent_name} {self.catalogue_no} {self.reagent_storage}"
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.reagent_name,
            "catalogue": self.catalogue_no,
            "url": self.catalogue_url,
            "storage": self.reagent_storage
        }