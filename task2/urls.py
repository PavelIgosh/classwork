from django.urls import path

from . import views

urlpatterns = [
    path('main', views.EvenListView.as_view(), name='main')
]
