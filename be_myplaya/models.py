from django.db import models

# Create your models here.
class RequestCall(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = "Request Call"
        verbose_name_plural = "Request Call"