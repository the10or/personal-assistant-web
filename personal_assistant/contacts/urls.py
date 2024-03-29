from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("<int:contact_id>/", views.contact_details, name="contact_details"),
    path("create/", views.create_or_edit_contact, name="create_contact"),
    path("edit/<int:contact_id>/", views.create_or_edit_contact, name="edit_contact"),
    path("upcoming_birthdays/", views.upcoming_birthdays, name="upcoming_birthdays"),
    path("search/", views.search_contacts, name="search_contacts"),
    path("delete/<int:contact_id>/", views.delete_contact, name="delete_contact"),
]
