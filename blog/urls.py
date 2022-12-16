from django.urls import path

from . import views

urlpatterns = [ 
    path('create-post/', views.createPost, name='create-post'),
    path('post/<int:pk>', views.viewPost, name='view-post'),
]