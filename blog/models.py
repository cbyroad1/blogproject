from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name