# Generated by Django 4.0.3 on 2022-07-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClimbingApp', '0002_climbedroute_route_userprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_routes',
            field=models.ManyToManyField(blank=True, related_name='profile_routes', to='ClimbingApp.climbedroute'),
        ),
    ]
