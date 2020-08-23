from django.shortcuts import render
from django.views.generic import  ListView
from .models import State
from json import dumps
# Create your views here.
class StateListView(ListView):
    model = State
    template_name = "qualified_majority_app/state_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dataJS = list()
        population_total, area_total = 0,0
        context['countries_num']  = len(context['object_list'])
        for obj in context['object_list']:
            dataJS.append([obj.name, obj.population, obj.territory])
            population_total+= obj.population
            area_total += obj.territory
        context['dataJS'] = dumps(dataJS)
        context['areaJS'] = area_total
        context['populationJS'] = population_total
        return context