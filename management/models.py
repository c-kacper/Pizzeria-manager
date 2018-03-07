from django.db import models
from management.choices import *


class Pizza(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField('Topping')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=32)
    size = models.CharField(max_length=32, choices=DRINK_SIZE_CHOICE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)


class Sauce(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)


class Salad(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)


class Customer(models.Model):
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)




