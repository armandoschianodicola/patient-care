from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.conf import settings

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
    model = models.Measure


class MeasureListView(ListView):
    model = models.Measure


class MeasureCreateView(CreateView):
    model = models.Measure
    fields = ['name', 'unit']

    def get_success_url(self):

        return reverse_lazy('measure-detail', kwargs={'pk': self.object.pk})


class PatientMeasureCreateView(CreateView):
    model = models.PatientMeasure
    fields = ['patient', 'measure', 'quantity']

    def get_success_url(self):

        return reverse_lazy('patient-detail', kwargs={'pk': self.object.pk})


class PatientMeasureListView(ListView):
    model = models.PatientMeasure


class MeasureUpdateView(UpdateView):
    model = models.Measure
    fields = ['name']


class MeasureDeleteView(DeleteView):
    model = models.Measure
    success_url = reverse_lazy('patient-care-home')


class UnitDetailView(DetailView):
    model = models.Unit


class UnitCreateView(CreateView):
    model = models.Unit
    fields = ['name']
    template_name_suffix = '_create_form'

    def get_success_url(self):

        return reverse_lazy('unit-detail', kwargs={'pk': self.object.pk})


class UnitUpdateView(UpdateView):
    model = models.Unit
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):

        return reverse_lazy('unit-detail', kwargs={'pk': self.object.pk})


class UnitListView(ListView):
    model = models.Unit


class UnitDeleteView(DeleteView):
    model = models.Unit
    success_url = reverse_lazy('patient-care-home')


def calculate_insulin(request):

    api_key = settings.SA_API_KEY

    if request.method == 'POST':
        pass
    else:
        pass

    context = {
        'form': 'form'
    }

    return render(request, "patient_care/calculate.html", context)
