from django.urls import path

from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("list/", views.file_list, name="file_list"),
    path("delete/<int:file_id>/", views.delete_file, name="delete_file"),
]
