from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'BookListLib.html'
