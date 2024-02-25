from django.urls import include, path
from . import views

app_name = "users_info"

urlpatterns = [
    path('', views.contact_list, name='dashboard_page'),
    path('edit', views.create_description, name='edit_user'),

]