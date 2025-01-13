from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Director

class DirectorListView(ListView):
    model = Director
    context_object_name = 'directors'
    template_name = 'DirectorView.html'