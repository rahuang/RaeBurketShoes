from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Test(models.Model):
    name = models.CharField(max_length=30)


class ShoppingCart(models.Model):
    pic = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)