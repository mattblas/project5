from re import U
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, userProfile


def index(request):
    if request.user.is_authenticated and not userProfile.objects.filter(profile_name=request.user).exists():
        return render(request, "ClimbingApp/update_profile.html", {
        "message": "Please update your profile."})
    else:
        return render(request, "ClimbingApp/index.html")

def update_profile(request):
    if request.method == "POST":
        try:
            pg = request.POST['form_profile_gender']
            pb = request.POST['form_profile_birth']
            b = userProfile(profile_name=request.user, profile_gender=pg, profile_birth=pb,)
            b.save()
            return render(request, "ClimbingApp/index.html", {
                "message": "Profile updated."
            })
        except:
            return render(request, "ClimbingApp/update_profile.html", {
                "message": "Something went wrong while updating profile. Try again.."
            })
    else:
        return render(request, "ClimbingApp/update_profile.html", {})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if userProfile.objects.filter(profile_name=request.user).exists():
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "ClimbingApp/update_profile.html", {
                "message": "Please update your profile."
            })
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
