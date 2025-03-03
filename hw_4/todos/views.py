from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def redirect_to_lists(request):
    return redirect('todo_lists')

def todo_list_view(request):
    lists = TodoList.objects.all()
    form = TodoListForm()
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    return render(request, 'todos/todo_lists.html', {'lists': lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todos.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', id=id)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def todo_list_edit(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/todo_list_edit.html', {'form': form, 'todo_list': todo_list})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_edit.html', {'form': form, 'todo': todo})
