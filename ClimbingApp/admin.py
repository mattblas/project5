from django.contrib import admin
from .models import Route, climbedRoute, userProfile
# Register your models here.

@admin.register(Route)
class User_routesAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'route_grade')

@admin.register(climbedRoute)
class User_routesAdmin(admin.ModelAdmin):
    list_display = ('climbed_route_name', 'climbed_route_date')

@admin.register(userProfile)
class User_routesAdmin(admin.ModelAdmin):
    list_display = ('profile_name', 'profile_gender', 'profile_birth', 'profile_active', 'profile_is_staff')