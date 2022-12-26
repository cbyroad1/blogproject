from django.urls import path

from . import views

urlpatterns = [ 
    path('create-post/', views.createPost, name='create-post'),
    path('post/<int:pk>', views.viewPost, name='view-post'),
    path('delete-post/<int:pk>/', views.deletePost, name='delete-post'),
    path('category/<int:pk>/', views.viewCategory, name='category-view'),
]