from django.shortcuts import render, redirect

# Create your views here
from django.contrib.auth.models import User
from .forms import UserForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Welcome to the Reservation System</h1>")
def get_users(request):
    users = list(User.objects.values())
    return jsonResponse(users, safe=False)

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'], password=data['password'])
        return JsonResponse({'id': user.id, 'username': user.username})

def create_user_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    
    return render(request, 'users/create_user.html', {'form': form})
@csrf_exempt
def get_user_details(request, id):
    try:
        user = User.objects.get(id=id)
        return jsonResponse({'id': user.id, 'username': user.username})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
