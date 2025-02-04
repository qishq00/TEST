from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, post_delete

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/delete/', post_delete, name='post-delete'),
]
