from django.urls import path
from .views import get_tables, create_table, table_list

urlpatterns = [
    path('tables/', get_tables, name='get_tables'),
    path('tables/', create_table, name='create_table'),
    path('', table_list, name='table_list'),

]