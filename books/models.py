from django.db import models

from core.models import BaseModel, BaseModelForm


# Create your models here.
class Book(BaseModel):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)


class BookForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Book
        fields = BaseModelForm.Meta.fields + ['name', 'content']
