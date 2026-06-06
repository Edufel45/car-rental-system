from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Car, BookingRequest

def home(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'cars/home.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def create_booking(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        booking = BookingRequest(
            car=car,
            customer_name=request.POST.get('name'),
            customer_email=request.POST.get('email'),
            customer_phone=request.POST.get('phone'),
            pickup_date=request.POST.get('pickup_date'),
            return_date=request.POST.get('return_date'),
            message=request.POST.get('message', '')
        )
        booking.save()
        return redirect('booking_success')
    
    return render(request, 'cars/booking_form.html', {'car': car})

def booking_success(request):
    return render(request, 'cars/success.html')