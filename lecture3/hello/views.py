from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") #renders so that html can be used

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name
    })

