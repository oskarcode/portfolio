from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import  StopForm, LineForm, StationForm
# Add your imports below:
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class HomeView(TemplateView):
  template_name = "routes/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["lines"] = Line.objects.all()
    context["stations"] = Station.objects.all()
    context["stops"] = Stop.objects.all()
    return context

class LinesView(ListView):
   model = Line
   template_name = 'routes/lines.html'

class CreateLineView(CreateView):
   model = Line
   form_class = LineForm
   template_name = 'routes/add_line.html'

class UpdateLineView(UpdateView):
   model = Line
   form_class = LineForm
   template_name = 'routes/update_line.html'

class DeleteLineView(DeleteView):
   model = Line
   template_name = 'routes/delete_line.html'
   success_url = '/lines'




class StationView(ListView):
          model = Station 
          template_name = 'routes/stations.html'


class CreateStationView(CreateView):
          model = Station 
          template_name = 'routes/add_station.html'
          form_class = StationForm

class UpdateStationView(UpdateView):
   model = Station
   form_class = StationForm
   template_name = 'routes/update_station.html'


class DeleteStationView(DeleteView):
   model = Station
   template_name = 'routes/delete_station.html'
   success_url = '/stations'





class StopView(ListView):
          model = Stop
          template_name = 'routes/stops.html'

class CreateStopView(CreateView):
          model = Stop
          template_name = 'routes/add_stop.html'
          form_class = StopForm

class UpdateStopView(UpdateView):
   model = Stop
   form_class = StopForm
   template_name = 'routes/update_stop.html'

class DeleteStopView(DeleteView):
   model = Stop
   template_name = 'routes/delete_stop.html'
   success_url = '/stops'