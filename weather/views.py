from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import DetailView
from django.http import Http404
from django.db.models import F, Func
from .forms import SearchBox
from .models import City
import requests
# Create your views here.
from django002.settings import WEATHER_API_KEY



def search_view(request):
    if request.method =="POST":
        form = SearchBox(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name == "":
               selected_city = City.objects.annotate(abs_diff=Func(F('lon')-form.cleaned_data["longitude"], function="ABS")).order_by('abs_diff').first()
               if form.cleaned_data["longitude"] is None:
                   selected_city = City.objects.annotate(abs_diff=Func(F('lat')-form.cleaned_data["latitude"], function="ABS")).order_by('abs_diff').first()
               return redirect(selected_city)
            if len(name)<2:
                raise Http404("Not Found")
            name = name[0].upper() + name[1::].lower()
            selected_city = City.objects.filter(name=name).first()
            if selected_city is None:
                return HttpResponse(content="Not Found")
            return redirect(selected_city)
    else:
        form = SearchBox()
    return render(request, "weather/search.html", {'form' : form})


class CityDetailView(DetailView):

    model = City
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payload = {"id": self.object.api_id, "appid":WEATHER_API_KEY, "units":"metric"}
        response = requests.get("http://api.openweathermap.org/data/2.5/weather",params=payload)
        print(response.url, payload.get("id"))
        context["temp"]=response.json().get('main').get("temp")
        context["feels_like"]=response.json().get('main').get("feels_like")
        context["pressure"]=response.json().get('main').get('pressure')
        context["humidity"]=response.json().get('main').get('humidity')
        context["icon_url"]="http://openweathermap.org/img/wn/"+ response.json().get('weather')[0].get('icon') +"@2x.png"
        context["wind_speed"]=response.json().get('wind').get("speed")
        print(context)
        return context
    