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

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^addpizza/$', PizzaAdd.as_view()),
    url(r'^addtopping/$', ToppingAdd.as_view()),
    url(r'^editpizza/(\d+)/$', PizzaEdit.as_view()),
    url(r'^edittopping/(\d+)/$', ToppingEdit.as_view()),
    url(r'^delete-topping/(\d+)/$', delete_topping),
    url(r'^delete-pizza/(\d+)/$', delete_pizza),
    url(r'^showpizzas/$', ShowPizza.as_view(), name='showpizzas'),
    url(r'^showtoppings/$', ShowTopping.as_view(), name='showtoppings'),


]
