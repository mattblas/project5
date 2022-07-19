from email import message
from urllib import response
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User, userProfile, Route

points_table = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4a": "4",
    "4b": "5",
    "4c": "6",
    "5a": "7",
    "5b": "8",
    "5c": "9",
    "6a": "10",
    "6a+": "11",
    "6b": "12",
    "6b+": "13",
    "6c": "14",
    "6c+": "15",
    "7a": "16",
    "7a+": "17",
    "7b": "18",
    "7b+": "19",
    "7c": "20",
    "7c+": "21",
    "8a": "22",
    "8a+": "23",
    "8b": "24",
    "8b+": "25",
    "8c": "26",
    "8c+": "27",
    "9a": "28",
    "9a+": "29",
    "9b": "30",
    "9b+": "31",
    "9c": "32",
}

def index(request):
    if request.user.is_authenticated and not userProfile.objects.filter(profile_name=request.user).exists():
        return render(request, "capstone/update_profile.html", {
        "message": "Please update your profile."})
    else:
        return render(request, "capstone/index.html")

def edit_route(request):
    return render(request, "capstone/staff.html", {})

def staff(request):
    all_routes = Route.objects.all()
    return render(request, "capstone/staff.html", {
        "all_routes": all_routes,
    })

def add_route(request):
    if request.method == "POST":
        rn = request.POST["form_route_name"]
        if Route.objects.filter(route_name = rn).exists():
            return render(request, "capstone/staff.html", {
        "message": "Route already exists"
        })
        else:      
            rg = request.POST["form_route_grade"]
            rp = int(points_table[rg])
            b = Route.objects.create(route_name = rn, route_grade = rg, route_points = rp)
            b.save()
            return render(request, "capstone/staff.html", {
                "message": "Route added successfully"
            })
    else: 
        return render(request, "capstone/staff.html", {})

def update_profile(request):
    if request.method == "POST":
        try:
            pg = request.POST['form_profile_gender']
            pb = request.POST['form_profile_birth']
            b = userProfile(profile_name=request.user, profile_gender=pg, profile_birth=pb,)
            b.save()
            return render(request, "capstone/index.html", {
                "message": "Profile updated."
            })
        except:
            return render(request, "capstone/update_profile.html", {
                "message": "Something went wrong while updating profile. Try again.."
            })
    else:
        return render(request, "capstone/update_profile.html", {})

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
                return render(request, "capstone/update_profile.html", {
                "message": "Please update your profile."
            })
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")

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
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("update_profile"))
    else:
        return render(request, "capstone/register.html")

def todo(request):
    return render(request, "capstone/todo.html")

def playground(request):
    return render(request, "capstone/playground.html")
