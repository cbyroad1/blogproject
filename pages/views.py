from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse
import boto3
import json

from .utils import send_email
from .forms import ContactForm

# Create your views here.
from blog.models import BlogPost, Category

def homepage(request):
    posts = BlogPost.objects.all().order_by('-date_created').annotate(number_of_comments = Count('comments'))
    categories = Category.objects.all()

    context = {'posts':posts, 'categories': categories}
    return render(request, 'index.html', context)

def blogposttest(request):
    return render(request, 'blogpost.html')

def contactpage(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            try:
                send_email(email, subject, message)
                return redirect('home')
            
            except:
                print("there was an error sending the info to lambda")
        else:
            print("The form is not valid!")
            
    context = {'form':form}

    return render(request, 'contact.html', context)
