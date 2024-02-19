from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/create/', views.create_or_edit_contact, name='create_contact'),
    path('contacts/edit/<int:contact_id>/', views.create_or_edit_contact, name='edit_contact'),
    path('contacts/upcoming_birthdays/', views.upcoming_birthdays, name='upcoming_birthdays'), 
    path('contacts/search/', views.search_contacts, name='search_contacts'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]