from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('name','username', 'email','date_joined')  # Include 'is_seller' in the list_display
    search_fields = ('username', 'email', 'name')
    ordering = ('date_joined',)

    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','username', 'email','password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
