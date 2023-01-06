from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.lastname, self.firstname)

    def get_absolute_url(self):

        return reverse('patient-detail', kwargs={'pk': self.pk})


class Measure(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PatientMeasure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
