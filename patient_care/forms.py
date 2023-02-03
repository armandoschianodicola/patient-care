from django.forms import ModelForm, TextInput, modelformset_factory

from . import models

IngredientCalculationFormSet = modelformset_factory(
    models.IngredientCalculation,
    fields=('ingredient', 'quantity', ),
    extra=1
)

# class IngredientCalculationForm(ModelForm):
#     class Meta:
#         model = models.IngredientCalculation
#         fields = ('ingredient', 'quantity', )
#         widgets = {
#             'quantity': TextInput(attrs={'placeholder': 'Aggiungi Quantità'}),
#         }
