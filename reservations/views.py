from django.shortcuts import render, redirect

# Create your views here.
from django.http import JsonResponse
from .forms import ReservationForm
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reservation
from tables.models import Table
from django.contrib.auth.models import User

def get_reservation(reqyest, id):
    try:
        reservation = Reservation.objects.get(id=id)
        return JsonResponse({'id': reservation.id, 'user': reservation.user.username, 'table': reservation.table.number, 'date': reservation.date, 'status': reservation.status})
    except Reservation.DoesNotExist:
        return JsonPesponse({'error': 'Reservation not found'}, status=404)

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        table = Table.objects.get(id=data['table_id'])
        reservation = Reservation.objects.create(user=user, table=table, date=data['date'], status="pending")
        return JsonResponse({'id': reservation.id, 'user': reservation.user.username, 'table': reservation.table.number, 'date': reservation.date, 'status': reservation.status})

def create_reservation_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reservations/create_reservation.html', {'form': form})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})
