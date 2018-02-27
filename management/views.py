from django.shortcuts import render
from django.views import View
from management.models import Pizza, Topping
from django.http import HttpResponse
from .forms import PizzaForm, ToppingForm


class PizzaAdd(View):
    def get(self, request):
        form = PizzaForm()
        return render(request, "add_pizza.html", {'form': form})

    def post(self, request):
        form = PizzaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            new_pizza = Pizza.objects.create(name=name, price=price)
            for topping in form.cleaned_data.get('toppings'):
                new_pizza.toppings.add(topping)
            return HttpResponse("dodano")


class ToppingAdd(View):
    def get(self, request):
        form = ToppingForm
        return render(request, "add_topping.html", {'form': form})

    def post(self, request):
        form = ToppingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            Topping.objects.create(name=name, price=price)
            return HttpResponse('dodano')


class ShowPizza(View):
    def get(self, request):
        pizza = Pizza.objects.all()
        ctx = {
            'pizzas': pizza,
        }
        return render(request, "show_pizza.html", ctx)

class ShowTopping(View):
    def get(self, request):
        topping = Topping.objects.all()
        ctx = {
            'toppings': topping,
        }
        return render(request, "show_topping.html", ctx)
