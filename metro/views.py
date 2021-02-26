from django.shortcuts import render
from django.views.generic.base import View
from .models import Station


class StationView(View):
    def get(self, request):
        stations = Station.objects.all()
        return render(request, "metro/metro_list.html", {'stations_list':stations})