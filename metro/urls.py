from django.urls import path

from .views import *

urlpatterns = [
    path("metro_stations", StationView.as_view())
]