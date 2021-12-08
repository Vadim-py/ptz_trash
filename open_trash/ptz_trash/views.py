from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

import folium
from folium import plugins

def index(request):
    return render(request, "index.html")

def info(request):
    return render(request, 'info.html')

def contact(request):
    return render(request, 'contact_info.html')



class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('success_page')
    template_name = 'contact_form.html'

def success(request):
   return HttpResponse('Письмо отправлено!')