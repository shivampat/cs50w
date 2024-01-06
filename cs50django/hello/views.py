from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def greeting(request, name): 
    return render(request, "hello/greeting.html", context= {
        "name": name.capitalize() 
    })