from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        import users.signals  # noqa
        from .models import Profile

        from django.contrib import admin

        admin.site.register(Profile)
