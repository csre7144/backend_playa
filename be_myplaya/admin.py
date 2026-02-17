from django.contrib import admin
from .models import RequestCall

# Register your models here.
@admin.register(RequestCall)
class HomeReuqestCall(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'message')