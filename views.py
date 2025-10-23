from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

import folium

from .models import Point, Route
from .forms import NewRouteForm

from .logic.business import find_routes
# Create your views here.


class PointsView(generic.ListView):
    template_name = 'guide/points.html'
    context_object_name = 'points'

    def get_queryset(self):
        return Point.objects.all()


def routes(request):
    context = {
        'routes': Route.objects.filter(Q(user_id=request.user.id) | Q(user_id__isnull=True)).order_by('-created')
    }
    return render(request, 'guide/routes.html', context)


def new_routes(request, route_length: int | float, required_point: Point = None):
    all_points = list(Point.objects.all())
    entry_point = [x for x in all_points if x.is_entry_point][0]
    built_routes = find_routes(all_points, entry_point, route_length, required_point)
    all_routes = Route.objects.filter(Q(user_id=request.user.id) | Q(user_id__isnull=True)).order_by('-created')


class PointView(generic.DetailView):
    model = Point
    template_name = 'guide/point.html'


class RouteView(generic.DetailView):
    model = Route
    template_name = 'guide/route.html'


def route(request):
    m = folium.Map(location=[55.8325, 37.6282],
                   zoom_start=15,
                   zoom_control=False,
                   control_scale=True,
                   width=800,
                   height=600)
    iframe = m.get_root()._repr_html_()


def new_route_params(request):
    if request.method == 'POST':
        form = NewRouteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('routes')
    else:
        form = NewRouteForm()
    return render(request, 'guide/index.html', {'form': form,  })





def register(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)

# def login(request):
#     if request.POST == 'POST':
#