from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"