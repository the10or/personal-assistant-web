# users\signals.py
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):

    city = models.CharField(max_length=100, blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)  # Додайте поле електронної пошти
    contacts = models.CharField(max_length=100, blank=True)
    files = models.FileField(upload_to='media/profile_files', blank=True, null=True)
    avatar = models.ImageField(default='media/default_avatar.png', upload_to='media/profile_images')
    # status = models.CharField(max_length=100, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)


    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            img = Image.open(self.avatar.path)

            if img.height > 250 or img.width > 250:
                new_img_size = (250, 250)
                img.thumbnail(new_img_size)
                img.save(self.avatar.path)
        except IOError as err:
            raise IOError('Виникла помилка при збережинні фото') from err
        