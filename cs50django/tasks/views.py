from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

tasks = ["foo", "bar", "faz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task:")

def index(request): 
    if "tasks" not in request.session: 
        request.session["tasks"] = []
    return render(request, "tasks\index.html", context={
        "tasks": request.session["tasks"]
    })

def addTask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks\\add.html", context={
                "form": form
            })

    return render(request, "tasks\\add.html", context={
        "form": NewTaskForm()
    })