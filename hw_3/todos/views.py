from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .forms import TodoForm

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo-list')
