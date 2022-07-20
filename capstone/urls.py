
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("update_profile", views.update_profile, name="update_profile"),
    path("staff", views.staff, name="staff"),
    path("add_route", views.add_route, name="add_route"),
    path("edit_route", views.edit_route, name="edit_route"),

    # API routes
    path("edit_route_form/<id>", views.edit_route_form, name="edit_route_form"),
    path("edit_route_submit", views.edit_route_submit, name="edit_route_submit"),

    # Shit to delate
    path("todo", views.todo, name="todo"),
    path("playground", views.playground, name="playground"),
    


    
]
