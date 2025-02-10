from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Получение всех постов
def get_posts(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)

# Получение одного поста
def get_post(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse({'title': post.title, 'description': post.description, 'author': post.author})

# Создание поста через Django Forms
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')  # Перенаправляем после создания
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})

# Удаление поста
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/posts/')  # После удаления перенаправляем
