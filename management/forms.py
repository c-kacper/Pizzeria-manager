from django.forms import ModelForm, forms
from .models import Pizza, Topping, Drink, Sauce, Salad
from django import forms
from management.choices import *

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        widgets = {
            'toppings': forms.CheckboxSelectMultiple,
        }


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = '__all__'


class DrinkForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DrinkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Drink
        fields = '__all__'
        widgets = {
            'size': forms.Select,
        }


class SauceForm(ModelForm):
    class Meta:
        model = Sauce
        fields = '__all__'


class SaladForm(ModelForm):
    class Meta:
        model = Salad
        fields = '__all__'
