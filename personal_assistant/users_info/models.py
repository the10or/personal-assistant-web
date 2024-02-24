from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True,)
    description = models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name_plural = "Users"
        ordering = ['username']
