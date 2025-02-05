from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, todo_delete

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/new/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/delete/', todo_delete, name='todo-delete'),
]
