from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def track(request):
    return render(request, "track.html")


def contact(request):
    return render(request, "contact.html")
