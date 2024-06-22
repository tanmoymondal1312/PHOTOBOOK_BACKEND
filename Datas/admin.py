from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking

class BookingUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Customize fields displayed in the admin list view
    # Example adjustments to avoid errors
    filter_horizontal = []  # Remove filter_horizontal if not needed for Booking
    ordering = ['name', 'created_at']  # Adjust ordering based on existing fields in Booking
    list_filter = ['name']  # Adjust list_filter based on existing fields in Booking

admin.site.register(Booking, BookingUserAdmin)
