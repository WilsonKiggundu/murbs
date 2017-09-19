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
