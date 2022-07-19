
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("update_profile", views.update_profile, name="update_profile"),

    path("todo", views.todo, name="todo"),
    path("playground", views.playground, name="playground"),
    path("staff", views.staff, name="staff"),
]
