from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from . import models


def home(request):

    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, "recipes/home.html", context=context)


class PatientDetailView(DetailView):
    model = models.Patient


class PatientListView(ListView):
    model = models.Patient
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class PatientCreateView(CreateView):
    model = models.Patient
    fields = ['firstname', 'lastname']


class PatientUpdateView(UpdateView):
    model = models.Patient
    fields = ['firstname', 'lastname']


class MeasureDetailView(DetailView):
    model = models.Patient


class MeasureListView(ListView):
    model = models.Patient


class MeasureCreateView(CreateView):
    model = models.Patient
    fields = ['name', 'quantity', 'unit']


class MeasureDeleteView(DeleteView):
    model = models.Measure
    success_url = reverse_lazy('recipes-home')
