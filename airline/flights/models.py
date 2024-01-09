from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.fields.CharField(max_length=3)
    city = models.fields.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code.upper()})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name="departures", on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name="arrivals", on_delete=models.CASCADE)
    duration = models.fields.IntegerField()

    def __str__(self):
        return f"{self.id}: Flight of duration {self.duration} from {self.origin} to {self.destination}"

class Passenger(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"    
