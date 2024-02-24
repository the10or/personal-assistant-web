from django.contrib import admin
from .models import Contact

admin.site.register(Contact)


class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)