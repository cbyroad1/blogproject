from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def blogposttest(request):
    return render(request, 'blogpost.html')