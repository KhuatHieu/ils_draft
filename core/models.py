from django.db import models
from django.forms import ModelForm
from django.utils import timezone

from core.managers import SoftDeletionManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeletionManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class BaseModelForm(ModelForm):
    class Meta:
        model = BaseModel
        fields = []
