from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost, Category

def homepage(request):
    posts = BlogPost.objects.all().order_by('-date_created')
    categories = Category.objects.all()

    context = {'posts':posts, 'categories': categories}
    return render(request, 'index.html', context)


def blogposttest(request):
    return render(request, 'blogpost.html')