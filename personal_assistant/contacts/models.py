from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.DO_NOTHING, related_name="created_contacts"
    )
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        "auth.User", on_delete=models.DO_NOTHING, related_name="modified_contacts"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
