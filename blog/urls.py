"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  blog.views import CreatePostView, ListPostsView

urlpatterns = [
     path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('posts/', ListPostsView.as_view(), name='list_posts_all'),
    path('posts/<int:post_id>/', ListPostsView.as_view(), name='list_posts'),

]
  

