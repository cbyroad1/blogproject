from django.contrib import admin

# Register your models here.
from .models import BlogPost, Category, Comments

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Comments)

