from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.conf import settings

from . import models
from .mixins import RedirectParams, FormErrors, APIMixin


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


class IngredientCreateView(CreateView):
    model = models.Ingredient
    fields = ['name', 'carb_qty']
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse_lazy('ingredient-detail', kwargs={'pk': self.object.pk})


class IngredientDetailView(DetailView):
    model = models.Ingredient


class IngredientListView(ListView):
    model = models.Ingredient


class UnitUpdateView(UpdateView):
    model = models.Unit
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('unit-detail', kwargs={'pk': self.object.pk})


class IngredientUpdateView(UpdateView):
    model = models.Ingredient
    fields = ['name', 'carb_qty']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ingredient-detail', kwargs={'pk': self.object.pk})


class IngredientDeleteView(DeleteView):
    model = models.Ingredient
    success_url = reverse_lazy('ingredient-list')


class UnitListView(ListView):
    model = models.Unit
    context_object_name = 'units'


class UnitDeleteView(DeleteView):
    model = models.Unit
    success_url = reverse_lazy('patient-care-home')


def calculate_insulin(request):
    context = {}

    if request.method == 'POST':
        cat = request.POST.get("cat", None)
        query = request.POST.get("query", None)
        if cat and query:
            # return RedirectParams(url='calc-insulin', params={"cat": cat, "query": query})
            results = APIMixin(cat=cat, query=query).get_data()

            if results:
                context = {
                    "results": results,
                    "cat": cat,
                    "query": query,
                }

    return render(request, "patient_care/calculate.html", context)


def get_ingredient_info(request, ingredient_id):

    cat = 'ingredients-info'

    results = APIMixin(cat=cat, query=False, ingredient_id=ingredient_id).get_data()

    context = {}
    if results:
        context = {
            "results": results,
            "cat": cat,
        }

    return render(request, "patient_care/ingredient_form.html", context)
