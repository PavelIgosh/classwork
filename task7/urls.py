from django.urls import path

from . import views

urlpatterns = [
    path('main', views.DirectorListView.as_view(), name='main')
]
