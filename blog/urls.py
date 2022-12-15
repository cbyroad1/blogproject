from django.urls import path

from . import views

urlpatterns = [ 
    path('create-post/', views.createPost, name='create-post')
]