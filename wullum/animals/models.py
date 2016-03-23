from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Animals(models.Model):
    animal_name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    born = models.DateField('Født', editable=True, null=True)
    arrived = models.DateField('Ankommet', editable=True, null=True)
    departure = models.DateField('Afgang', editable=True, null=True, blank=True)
    dead = models.BooleanField('Død?', editable=True, default=False)
    animal_characteristics = models.TextField(max_length=400)
    fur_colour = models.CharField(max_length=100)
    fur_type = models.CharField(max_length=100)
    white_marks = models.CharField(max_length=100)
    eye_colour = models.CharField(max_length=100)
    blue_eyed_white = models.CharField(max_length=50)
    genotype = models.CharField(max_length = 50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        #if self.id is None:
           # self.slug = slugify(self.animal_name)
        self.slug = slugify(self.animal_name)
        super(Animals, self).save(*args, **kwargs)

    def __str__(self):
        return self.animal_name

    class Meta:
        verbose_name_plural = "Animals"

class Weights(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    weight_date = models.DateField('Dato vejet', editable=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "Weights"

class Comments(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    comments_date = models.DateField('Dato', editable=True, null=True)
    comment = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Comments"

class Fat(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    fat_date = models.DateField('Dato', editable=True, null=True)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Fat"

class FoodPurchases(models.Model):
    food_date = models.DateField('Dato for køb', editable=True, null=True)
    food_product = models.CharField(max_length=200)
    food_amount = models.DecimalField(max_digits=5, decimal_places=2)
    food_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "FoodPurchases"

class MiscPurchases(models.Model):
    misc_date = models.DateField('Dato for køb', editable=True, null=True)
    misc_product = models.CharField(max_length=300)
    misc_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "MiscPurchases"

class Eggs(models.Model):
    egg_date = models.DateField('Dato', editable=True, null=True)
    egg_amount = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Eggs"
