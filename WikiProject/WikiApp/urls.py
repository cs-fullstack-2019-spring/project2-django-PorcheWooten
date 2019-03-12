from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NewPosts/', views.NewPosts, name='NewPosts'),
    path('YourPosts/', views.YourPosts, name='YourPosts'),
]