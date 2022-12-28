from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .forms import BlogPostForm
from .models import BlogPost, Category

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
    return render(request, 'create_post.html', context)

def viewPost(request, pk):
    post = BlogPost.objects.get(id=pk)
    author = BlogPost.objects.values_list('author__username', flat=True).get(id=pk)
    # need to query for comments that only apply for the single blogpost
    comments = post.comments_set.all()

    
    context = {'post':post, 'author':author, 'comments':comments}
    return render(request, 'blogpost.html', context)

def deletePost(request, pk):
    post = BlogPost.objects.get(id=pk)
    author = BlogPost.objects.values_list('author__username', flat=True).get(id=pk)
    
    if request.method == 'POST':
        if author == request.user.username:
                post.delete()
                return redirect('home')
        else:
            messages.error(request, 'You are not authorized to do this')

    context = {'post':post, 'author':author}
    return render(request, 'delete_post.html', context)

def viewCategory(request, pk):
    category = Category.objects.get(id=pk)
    posts = category.blogpost_set.all()

    context = {'category':category, 'posts':posts}
    return render(request, 'categories.html', context)