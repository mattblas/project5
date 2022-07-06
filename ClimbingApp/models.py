from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import DateTimeField


class User(AbstractUser):
    pass

class Route(models.Model):
    route_name          = models.CharField(max_length=60, unique=True)
    route_grade         = models.CharField(max_length=5)

# class RoutePoints(models.Model):
#     route_points_grade  = models.ForeignKey(Route.route_grade, related_name="route_points_grade", on_delete=models.CASCADE)
#     route_points_points = models.IntegerField(related_name="route_points_points")

class climbedRoute(models.Model):
    climbed_route_name  = models.ForeignKey(Route, related_name="climbed_route_name", on_delete=models.CASCADE)
    climbed_route_date  = models.DateTimeField(auto_now_add=True) 

class userProfile(models.Model):
    profile_name        = models.ForeignKey(User, related_name="profile_name", on_delete=models.CASCADE)
    profile_gender      = models.CharField(max_length=30)
    profile_birth       = models.DateField()
    profile_active      = models.BooleanField(default=True)
    profile_is_staff    = models.BooleanField(default=False)
    profile_routes      = models.ManyToManyField(climbedRoute, related_name="profile_routes", default=None)
    # profile_avatar      = ???

