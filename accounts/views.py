from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.views import View

from .forms import UserRegistrationForm, UserLoginForm


class Register(View):
    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'register.html', context={"form": form})

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'register.html', context={"form": form})


class Login(View):
    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Неверное имя пользователя или пароль")
        return render(request, 'login.html', context={"form": form})

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', context={"form": form})


class Logout(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


def index(request):
    return render(request, 'home.html')
