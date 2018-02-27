from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField('Topping')


class Topping(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)




