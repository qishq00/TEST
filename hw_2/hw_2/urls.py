"""
URL configuration for hw_2 project.

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
from django.shortcuts import render
from movie.models import Movie
from blog.models import Article

# Представление для главной страницы
def home(request):
    movies = Movie.objects.all()
    articles = Article.objects.all()
    return render(request, "home.html", {"movies": movies, "articles": articles})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Главная страница с фильмами и статьями
    path('api/', include('movie.urls')),
    path('api/', include('blog.urls')),
]

