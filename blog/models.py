from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from accounts.models import CustomUser


class BlogPost(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


