from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost

def homepage(request):
    posts = BlogPost.objects.all().order_by('-date_created')

    context = {'posts':posts}
    return render(request, 'index.html', context)


def blogposttest(request):
    return render(request, 'blogpost.html')