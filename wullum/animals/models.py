from django.db import models

# Create your models here.
class Animals(models.Model):
    animal_name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    born = models.DateField
    arrived = models.DateField
    departure = models.DateField
    dead = models.BooleanField
    animal_characteristics = models.TextField(max_length=400)
    fur_colour = models.CharField(max_length=100)
    fur_type = models.CharField(max_length=100)
    white_marks = models.CharField(max_length=100)
    eye_colour = models.CharField(max_length=100)
    blue_eyed_white = models.CharField(max_length=50)
    genotype = models.CharField(max_length = 50)

class Weights(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    weight_date = models.DateField
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Comments(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    comments_date = models.DateField
    comment = models.TextField(max_length=500)

class Fat(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    fat_date = models.DateField
    description = models.CharField(max_length=100)

class FoodPurchases(models.Model):
    food_date = models.DateField
    food_product = models.CharField(max_length=200)
    food_amount = models.DecimalField(max_digits=5, decimal_places=2)
    food_price = models.DecimalField(max_digits=7, decimal_places=2)

class MiscPurchases(models.Model):
    misc_date = models.DateField
    misc_product = models.CharField(max_length=300)
    misc_price = models.DecimalField(max_digits=7, decimal_places=2)

class Eggs(models.Model):
    egg_date = models.DateField
    egg_amount = models.IntegerField(default=0)
