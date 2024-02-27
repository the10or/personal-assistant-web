from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default="user")
    company = models.CharField(max_length=100, default="")


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    instance.employee.save()
