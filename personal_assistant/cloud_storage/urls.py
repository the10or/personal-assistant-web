from django.urls import path

from . import views

app_name = "cloud_storage"

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("list/", views.file_list, name="file_list"),
    path("list/<str:category>/", views.file_list, name="file_list_category"),
    path("delete/<int:file_id>/", views.delete_file, name="delete_file"),
]
