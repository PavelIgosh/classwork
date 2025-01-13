from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Event

class EvenListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'EventList.html'