from django.forms import ModelForm, TextInput

from . import models


class IngredientCalculationForm(ModelForm):
    class Meta:
        model = models.IngredientCalculation
        fields = ('ingredient', 'quantity', )
        widgets = {
            'quantity': TextInput(attrs={'placeholder': 'Aggiungi Quantità'}),
        }
