from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class RequestCall(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region="US")
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = "Request Call"
        verbose_name_plural = "Request Call"


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class TransferRX(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(region="US")

    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    pharmacy_name = models.CharField(max_length=150)
    pharmacy_phone_number = PhoneNumberField(region="US")
    rx_number = models.CharField(max_length=100)


    medicine_first_letters = models.CharField(max_length=3)
    medicine_needed_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rx_number}"
    
    phone_number = PhoneNumberField(
        region="US",
        error_messages={"invalid": "Enter a valid US phone number"}
    )

    pharmacy_phone_number = PhoneNumberField(
        region="US",
        error_messages={"invalid": "Enter a valid US pharmacy phone number"}
    )
    
    class Meta:
        verbose_name = "Transfer RX"
        verbose_name_plural = "Transfer RX"

