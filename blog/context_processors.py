from .models import Category, BlogPost

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def posts(request):
    return {
        'posts': BlogPost.objects.all()
    }

