from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('booking/<int:car_id>/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
]