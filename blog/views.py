from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .forms import BlogPostForm
from .models import BlogPost

def createPost(request):
    form = BlogPostForm()

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'There was an error creating your post. Please try again')

    context = {'form':form}
    return render(request, 'create-post.html', context)

def viewPost(request, pk):
    post = BlogPost.objects.filter(id=pk)
    
    context = {'post':post}
    return render(request, 'blogpost.html', context)