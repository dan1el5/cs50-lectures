from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #RIGHT NOW THERE IS NOTHING ON THE DEFAULT PAGE
    path("<str:name>", views.greet, name="greet"), #this path allows any name to be put in and it will return hello (name)
]
