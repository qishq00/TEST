from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Table

def get_tables(request):
    tables = list(table.objects.values())
    return JsonResponse(tables, safe=False)

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(number=gata['number'], seats=data['seats'], is_available=data.get('is_available'))
        return JsonResponse({'id': table.id, 'number': table.number, 'seats': table.seats, 'is_available': table.is_available})

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/table_list,html', {'tables': tables})
