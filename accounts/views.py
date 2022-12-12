from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

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

