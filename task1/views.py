from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Book, Genre, Author


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'BookList.html'
