from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from management.models import Pizza, Topping, Drink, Sauce, Salad
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PizzaForm, ToppingForm, DrinkForm, SauceForm, SaladForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

html = """<form action="/home">
    <input type="submit" value="Back" />
</form>"""

# 1. usuwanie obiektow i zmiana dostępności jest takie same, można je zrobić w
# jednej funkcji zamiast duplikować kod

# --------------- PIZZA ---------------


class PizzaAdd(View):
    def get(self, request):
        form = PizzaForm
        return render(request, "add_pizza.html", {'form': form})

    def post(self, request):
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showpizzas')


class PizzaEdit(View):
    def get(self, request, id):
        pizza = get_object_or_404(Pizza, pk=id)
        form = PizzaForm(initial={'name': pizza.name,
                                  'price': pizza.price,
                                  'toppings': pizza.toppings.all,
                                  })
        return render(request, "add_pizza.html", {'form': form})

    def post(self, request, id):

        pizza = get_object_or_404(Pizza, pk=id)
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('showpizzas')

    def delete_pizza(self, id):
        emp = Pizza.objects.get(pk=id)
        emp.delete()
        return HttpResponse('deleted {}'.format(html))


class PizzaShow(View):
    def get(self, request):
        pizza = Pizza.objects.all().order_by('price')
        ctx = {
            'pizzas': pizza,
        }
        return render(request, "show_pizza.html", ctx)

# --------------- TOPPINGS ---------------


class ToppingAdd(View):
    def get(self, request):
        form = ToppingForm
        return render(request, "add_topping.html", {'form': form})

    def post(self, request):
        form = ToppingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtoppings')


class ToppingEdit(View):
    def get(self, request, id):
        topping = get_object_or_404(Topping, pk=id)
        form = ToppingForm(initial={'name': topping.name,
                                    'price': topping.price,
                                    })
        return render(request, "add_topping.html", {'form': form})

    def post(self, request, id):
        topping = Topping.objects.get(pk=id)
        form = ToppingForm(request.POST, instance=topping)
        if form.is_valid():
            form.save()
            return redirect('showtoppings')

    def delete_topping(self, id):
        emp = Topping.objects.get(pk=id)
        emp.delete()
        return HttpResponse('deleted {}'.format(html))


class ToppingShow(View):
    def get(self, request):
        topping = Topping.objects.all().order_by('price')
        ctx = {
            'toppings': topping,
        }
        return render(request, "show_topping.html", ctx)

# --------------- DRINKS ---------------


class DrinkAdd(View):
    def get(self, request):
        form = DrinkForm
        return render(request, "add_drink.html", {'form': form})

    def post(self, request):
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('dodano!')


class DrinkEdit(View):
    def get(self, request, id):
        drink = get_object_or_404(Drink, pk=id)
        form = DrinkForm(initial={'name': drink.name,
                                  'price': drink.price,
                                  'size': drink.size,
                                  })
        return render(request, "add_drink.html", {'form': form})

    def post(self, request, id):
        drink = get_object_or_404(Drink, pk=id)
        form = DrinkForm(request.POST, instance=drink)

        if form.is_valid():
            form.save()
            return redirect('showdrinks')

    def delete_drink(self, id):
        emp = Drink.objects.get(pk=id)
        emp.delete()
        return HttpResponse('deleted {}'.format(html))


class DrinkShow(View):
    def get(self, request):
        drink = Drink.objects.all().order_by('price')
        ctx = {
            'drinks': drink,
        }
        return render(request, "show_drink.html", ctx)

# --------------- SAUCE ---------------


class SauceAdd(View):
    def get(self, request):
        form = SauceForm
        return render(request, "add_sauce.html", {'form': form})

    def post(self, request):
        form = SauceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showsauces')


class SauceEdit(View):
    def get(self, request, id):
        sauce = get_object_or_404(Sauce, pk=id)
        form = SauceForm(initial={'name': sauce.name,
                                  'price': sauce.price,
                                  })
        return render(request, "add_sauce.html", {'form': form})

    def post(self, request, id):
        sauce = Sauce.objects.get(pk=id)
        form = SauceForm(request.POST, instance=sauce)

        if form.is_valid():
            form.save()
            return redirect('showsauces')

    def delete_sauce(self, id):
        emp = Sauce.objects.get(pk=id)
        emp.delete()
        return HttpResponse('deleted {}'.format(html))


class SauceShow(View):
    def get(self, request):
        sauce = Sauce.objects.all().order_by('price')
        ctx = {
            'sauces': sauce,
        }
        return render(request, "show_sauce.html", ctx)

# --------------- SALAD ---------------


class SaladAdd(View):
    def get(self, request):
        form = SaladForm
        return render(request, "add_salad.html", {'form': form})

    def post(self, request):
        form = SaladForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showsalads')


class SaladEdit(View):
    def get(self, request, id):
        salad = get_object_or_404(Salad, pk=id)
        form = SaladForm(initial={'name': salad.name,
                                  'price': salad.price,
                                  'description': salad.description,
                                  })
        return render(request, "add_salad.html", {'form': form})

    def post(self, request, id):
        salad = Salad.objects.get(pk=id)
        form = SaladForm(request.POST, instance=salad)

        if form.is_valid():
            form.save()
            return redirect('showsalads')

    def delete_salad(self, id):
        emp = Salad.objects.get(pk=id)
        emp.delete()
        return HttpResponse('deleted {}'.format(html))


class SaladShow(View):
    def get(self, request):
        salad = Salad.objects.all().order_by('price')
        ctx = {
            'salads': salad,
        }
        return render(request, "show_salad.html", ctx)


class MenuShow(View):
    def get(self, request):
        pizza = Pizza.objects.all().filter(available=True).order_by('price')
        drink = Drink.objects.all().filter(available=True).order_by('price')
        sauce = Sauce.objects.all().filter(available=True).order_by('price')
        salad = Salad.objects.all().filter(available=True).order_by('price')
        ctx = {
            'pizzas': pizza,
            'drinks': drink,
            'sauces': sauce,
            'salads': salad,
        }
        return render(request, 'home.html', ctx)




# def index(request):
#     return render(request, 'home.html')


