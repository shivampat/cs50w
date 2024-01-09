from django.urls import path, reverse

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("<int:flight_id>", views.flight, name="flight"), 
]