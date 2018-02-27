from django.forms import ModelForm, forms
from .models import Pizza, Topping
from django import forms


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
