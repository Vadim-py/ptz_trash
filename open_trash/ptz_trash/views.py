from django.shortcuts import render
import folium
from folium import plugins

def index(request):
    return render(request, "index.html")

