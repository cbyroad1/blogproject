from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.

from . import forms

def signUpPage(request):
    
    form = forms.CustomUserCreationForm()

    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            print('sucess')
            return redirect('home')
            
        else:
            messages.error(request, 'An error occured during registration')

    context = {'form':form}
    return render(request, 'accounts/signup.html', context)


def loginPage(request):
    form = forms.LoginForm()

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            get_user_model().objects.get(username=username)
        except:
            messages.error(request, 'This username is already taken')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'There was an error logging you in')            

    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def logout_user(request):

    logout(request)
    return redirect(reverse('home'))