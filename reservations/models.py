from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tables.models import Table






class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.date} ({self.status})'