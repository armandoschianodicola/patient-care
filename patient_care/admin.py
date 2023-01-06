from django.contrib import admin
from . import models


class PatientMeasureInLine(admin.TabularInline):
    model = models.PatientMeasure


class MeasureAdmin(admin.ModelAdmin):
    inlines = [PatientMeasureInLine]
    extra = 0
    # readonly_fields = ['created', 'modified']


# Register your models here.
admin.site.register(models.Patient, MeasureAdmin)
admin.site.register(models.Unit)
admin.site.register(models.Measure)
