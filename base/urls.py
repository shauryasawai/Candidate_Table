from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumni_list, name='alumni_list'),
    path('add/', views.add_alumni, name='add_alumni'),
    path('edit/<int:alumni_id>/', views.edit_alumni, name='edit_alumni'),
    path('delete/<int:alumni_id>/', views.delete_alumni, name='delete_alumni'),
]
