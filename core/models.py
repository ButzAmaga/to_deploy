from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"