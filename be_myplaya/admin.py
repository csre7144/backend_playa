from django.contrib import admin
from .models import RequestCall,Contact, TransferRX

# Register your models here.
@admin.register(RequestCall)
class HomeReuqestCall(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'message')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'created_at')

@admin.register(TransferRX)
class TransferRXAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'address_line_1', 'city', 'state', 'zip_code', 'pharmacy_name', 'pharmacy_phone_number', 'rx_number', 'medicine_first_letters', 'medicine_needed_date', 'created_at')