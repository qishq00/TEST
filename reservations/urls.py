from django.urls import path
from .views import get_reservation, create_reservation, create_reservation_view, reservation_list

urlpatterns = [
    path('reservations/<int:id>/', get_reservation, name='get_reservation'),
    path('reservations/', create_reservation, name='create_reservation'),
    path('create/', create_reservation_view, name='create_reservation'),
]
urlpatterns += [
    path('', reservation_list, name='reservation_list'),
]