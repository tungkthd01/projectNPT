"""ProjectBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import  BlogUpload,BlogUserView,CategoryAllView,BlogAllView,BlogAllDetailView,CategoryAllDetailView
urlpatterns = [
    path("", BlogAllView.as_view(),name = "view_blog"),
    path("<int:pk>/", BlogAllDetailView.as_view(), name = "view_detail_blog"),
    path("creteblog/", BlogUpload.as_view(), name= "create_blog"),
    path("category/", CategoryAllView.as_view(), name= "category"),
    path("blog/", BlogUserView.as_view(),name= "blog_user"),
    path("category/<int:pk>",CategoryAllDetailView.as_view(), name="category_detail"),
]
