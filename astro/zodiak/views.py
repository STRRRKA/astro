from django.shortcuts import render
from urllib.request import urlopen
from .models import star
# Create your views here.
def index(request):
    return render (request, 'index.html', )

def circle(request):
    return render(request, 'circle.html')

def stars(request):
    stars = star.objects.all()
    return render(request, 'stars.html', {'stars':stars})