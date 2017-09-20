from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "users/login.html", {
        'title': 'Login'
    })


def details(request):
    return render(request, "users/details.html", {
        'title': 'Login'
    })


def register(request):
    return render(request, "users/signup.html", {
        'title': 'Register'
    })


def recover_password(request):
    return render(request, "users/recover-password.html", {
        'title': 'Reset Password'
    })
