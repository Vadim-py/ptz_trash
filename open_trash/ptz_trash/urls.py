from django.urls import path
from .views import ContactForm, success, index, info, ContactCreate


urlpatterns = [
    path('', index),
    path('info', info),
    path('contact', ContactCreate.as_view(),  name='contact_page'),
    path('success', success, name='success_page'),
]