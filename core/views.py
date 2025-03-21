from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeat_password = request.POST["repeat_password"]
        if password != repeat_password:
            return render(request, 'core/sign_up.html',{"error": "loгин или пароль не совподают"})
    return render(request, 'core/sign_up.html')

def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("catalog")
        else:
            return render(request, 'core/sign_in.html',{"error": "неверно логин или пароль"})
    return render(request, 'core/sign_in.html')

def profile(request):
    return render(request, 'core/profile.html')