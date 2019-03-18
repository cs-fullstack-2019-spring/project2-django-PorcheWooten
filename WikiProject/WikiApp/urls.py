from django.urls import path, include
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('NewPosts/', views.NewPosts, name='NewPosts'),
    path('NewUser/', views.NewUser, name='NewUser'),
    path('YourPosts/', views.YourPosts, name='YourPosts'),
    path('newRelatedPost/post_id', views.newRelatedPost, name='newRelatedPost'),
    path('viewpost/<int:post_id>/', views.viewpost, name='viewpost'),
    path('editPost/<int:post_id>/', views.editPost, name='editPost'),
    path('editRelatedItem/<int:item_id>/', views.editRelatedItem, name='editRelatedItem'),
    path('deletePost/<int:post_id>/', views.deletePost, name='deletePost'),
    path('deleteRelatedItem/<int:item_id>/', views.deleteRelatedItem, name='deleteRelatedItem'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('images/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]
