from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointmentpage , name='appointmentpage'),
    path('doctors/',views.selectslot,name='selectslot'),
    path('doctors/doc/',views.booknow,name='booknow'),
]
