from django.shortcuts import render

# Create your views here.
from .forms import LoginForm


def login(request):
    form = LoginForm()

    return render(request, "users/login.html", {
        'title': 'Login',
        'form': form
    })


def details(request):
    return render(request, "users/details.html", {
        'title': 'Profile'
    })


def register(request):
    return render(request, "users/signup.html", {
        'title': 'Register'
    })


def recover_password(request):
    return render(request, "users/recover-password.html", {
        'title': 'Reset Password'
    })


def logout(request):
    return render(request, "users/login.html", {
        'title': 'Login'
    })
