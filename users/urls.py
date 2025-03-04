from django.urls import path
from .views import get_users, create_user, get_user_details, user_list, create_user_view

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/', create_user, name='create_user'),
    path('users/<int:id>/', get_user_details, name='get_user_details'),
    path('', user_list, name='user_list'),
    path('create/', create_user_view, name='create_user'),
]