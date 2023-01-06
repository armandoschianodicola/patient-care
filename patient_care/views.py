from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from . import models


class PatientDetailView(DetailView):
    model = models.Patient


class PatientListView(ListView):
    model = models.Patient
    context_object_name = 'patients'


class PatientCreateView(CreateView):
    model = models.Patient
    fields = ['lastname', 'firstname']

    def form_valid(self, form):

        # form.instance.author = self.request.user

        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = models.Patient
    fields = ['firstname', 'lastname']


class MeasureDetailView(DetailView):
    model = models.Patient


class MeasureListView(ListView):
    model = models.Patient


class MeasureCreateView(CreateView):
    model = models.Measure
    fields = ['name', 'unit']


class PatientMeasureCreateView(CreateView):
    model = models.PatientMeasure
    fields = ['name', 'quantity', 'unit']


class MeasureUpdateView(UpdateView):
    model = models.Measure
    fields = ['name', 'quantity', 'unit']


class MeasureDeleteView(DeleteView):
    model = models.Measure
    success_url = reverse_lazy('recipes-home')


class UnitCreateView(CreateView):
    model = models.Unit
    fields = ['name']
