from django.contrib import admin
from .models import CustomUser, Role

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    



