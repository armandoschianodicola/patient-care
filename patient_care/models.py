from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Patient(TimeStampedModel, models.Model):
    firstname = models.CharField('Nome', max_length=100)
    lastname = models.CharField('Cognome', max_length=100)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}.'.format(self.lastname, self.firstname[:1])

    def get_absolute_url(self):

        return reverse('patient-detail', kwargs={'pk': self.pk})


class Unit(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Measure(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Ingredient(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    carb_qty = models.FloatField('Carboidrati')

    def __str__(self):
        return self.name


class PatientMeasure(TimeStampedModel, models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    quantity = models.FloatField('Quantità')


class IngredientCalculation(TimeStampedModel, models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField('Quantità')
