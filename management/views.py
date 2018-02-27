from django.shortcuts import render, redirect
from django.views import View
from management.models import Pizza, Topping
from django.http import HttpResponse, HttpResponseRedirect
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
            #return HttpResponse("dodano")
            #return HttpResponseRedirect('/showpizzas/')
            return redirect('showpizzas')


class PizzaEdit(View):
    def get(self, request, id):
        pizza = Pizza.objects.get(pk=id)
        form = PizzaForm(initial={'name': pizza.name,
                                  'price': pizza.price,
                                  'toppings': pizza.toppings.all,
                                  })
        return render(request, "add_pizza.html", {'form': form})

    def post(self, request, id):
        form = PizzaForm(request.POST)
        pizza = Pizza.objects.get(pk=id)
        if form.is_valid():
            pizza.name = form.cleaned_data['name']
            pizza.price = form.cleaned_data['price']
            pizza.save()
            pizza.toppings.clear()
            for topping in form.cleaned_data.get('toppings'):
                pizza.toppings.add(topping)
            #return HttpResponse("Edytowano")
            #return HttpResponseRedirect('/showpizzas/')
            return redirect('showpizzas')


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
            #return HttpResponse('dodano')
            return redirect('showtoppings')


class ToppingEdit(View):
    def get(self, request, id):
        topping = Topping.objects.get(pk=id)
        form = ToppingForm(initial={'name': topping.name,
                                    'price': topping.price,
                                    })
        return render(request, "add_topping.html", {'form': form})

    def post(self, request, id):
        form = ToppingForm(request.POST)
        topping = Topping.objects.get(pk=id)
        if form.is_valid():
            topping.name = form.cleaned_data['name']
            topping.price = form.cleaned_data['price']
            topping.save()
            #return HttpResponse("Edytowano")
            return redirect('showtoppings')


class ShowPizza(View):
    def get(self, request):
        pizza = Pizza.objects.all().order_by('price')
        ctx = {
            'pizzas': pizza,
        }
        return render(request, "show_pizza.html", ctx)


def delete_pizza(request, id):
    emp = Pizza.objects.get(pk=id)
    emp.delete()
    return HttpResponse('deleted')


class ShowTopping(View):
    def get(self, request):
        topping = Topping.objects.all().order_by('price')
        ctx = {
            'toppings': topping,
        }
        return render(request, "show_topping.html", ctx)


def delete_topping(request, id):
    emp = Topping.objects.get(pk=id)
    emp.delete()
    return HttpResponse('deleted')


def index(request):
    return render(request, 'home.html')
