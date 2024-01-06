from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("article/<str:title>/", views.getArticle, name="getArticle"),
    path("search/", views.search, name="search"),
    path("random/", views.randomEntry, name="random"),
    path("create/", views.create, name="create"),
]
