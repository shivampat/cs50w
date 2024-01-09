from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request): 
    return render(request, "flights/index.html", context={
        "flights": Flight.objects.all()
    })

def flight(request, flight_id): 
    return render(request, "flights/flight.html", context={
        "flight": Flight.objects.get(pk=flight_id)
    })