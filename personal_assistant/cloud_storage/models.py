from django.db import models


# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to="files/")
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="files"
    )
    category = models.CharField(max_length=255, default="other")

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file.name
