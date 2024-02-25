from django.urls import include, path
from . import views

app_name = "users_info"

urlpatterns = [
    path('', views.contact_list, name='dashboard_page'),
    path('edit_first_name', views.edit_first_name, name='edit_first_name'),
    path('edit_last_name', views.edit_last_name, name='edit_last_name'),
    path('edit_email', views.edit_email, name='edit_email'),
]