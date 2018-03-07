"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from management.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home/$', MenuShow.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^addpizza/$', PizzaAdd.as_view()),
    url(r'^addtopping/$', ToppingAdd.as_view()),
    url(r'^adddrink/$', DrinkAdd.as_view()),
    url(r'^addsauce/$', SauceAdd.as_view()),
    url(r'^addsalad/$', SaladAdd.as_view()),
    url(r'^editpizza/(\d+)/$', PizzaEdit.as_view()),
    url(r'^edittopping/(\d+)/$', ToppingEdit.as_view()),
    url(r'^editdrink/(\d+)/$', DrinkEdit.as_view()),
    url(r'^editsauce/(\d+)/$', SauceEdit.as_view()),
    url(r'^editsalad/(\d+)/$', SaladEdit.as_view()),
    url(r'^delete-pizza/(\d+)/$', PizzaEdit.delete_pizza),
    url(r'^delete-topping/(\d+)/$', ToppingEdit.delete_topping),
    url(r'^delete-drink/(\d+)/$', DrinkEdit.delete_drink),
    url(r'^delete-sauce/(\d+)/$', SauceEdit.delete_sauce),
    url(r'^delete-salad/(\d+)/$', SaladEdit.delete_salad),
    url(r'^showpizzas/$', PizzaShow.as_view(), name='showpizzas'),
    url(r'^showtoppings/$', ToppingShow.as_view(), name='showtoppings'),
    url(r'^showdrinks/$', DrinkShow.as_view(), name='showdrinks'),
    url(r'^showsauces/$', SauceShow.as_view(), name='showsauces'),
    url(r'^showsalads/$', SaladShow.as_view(), name='showsalads'),
]



