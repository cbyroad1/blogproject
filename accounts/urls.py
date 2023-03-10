from django.urls import path

from . import views

urlpatterns = [ 
    path('signup/', views.signUpPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout_user, name='logout'),
]