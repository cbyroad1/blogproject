from django.forms import ModelForm, Textarea
from django import forms
#
from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','category', 'content']
