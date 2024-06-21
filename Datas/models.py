# Datas/models.py

from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone aware default value
    whatsapp_message_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking - {self.name} ({self.service})"
