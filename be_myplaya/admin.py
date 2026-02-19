from django.contrib import admin
from .models import RequestCall,Contact

# Register your models here.
@admin.register(RequestCall)
class HomeReuqestCall(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'message')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'created_at')