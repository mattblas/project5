from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


def index(request):
    return render(request, "ClimbingApp/index.html")

def update_profile(request):
    if request.user.is_authenticated:
        return render(request, "ClimbingApp/update_profile.html")
    else:
        return render(request, "ClimbingApp/register.html", {
            "message": "You are not registered. Please register."
        })    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ClimbingApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ClimbingApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ClimbingApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "ClimbingApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("update_profile"))
    else:
        return render(request, "ClimbingApp/register.html")

def todo(request):
    return render(request, "ClimbingApp/todo.html")

def playground(request):
    return render(request, "ClimbingApp/playground.html")
