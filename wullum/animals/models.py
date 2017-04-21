# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class Animals(models.Model):
    animal_name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    born = models.DateField('Født', editable=True, null=True, blank=True)
    arrived = models.DateField('Ankommet', editable=True, null=True)
    departure = models.DateField('Afgang', editable=True, null=True, blank=True)
    dead = models.BooleanField('Død?', editable=True, default=False)
    butchered = models.BooleanField('Slagtet?', editable=True, default=False)
    gone = models.BooleanField('Fjern', editable=True, default=False)
    deleted = models.BooleanField('Slettet', editable=True, default=False)
    sold = models.BooleanField('Solgt', editable=True, default=False)
    sold_price = models.DecimalField('Pris', editable=True, max_digits=7, decimal_places=2, null=True, blank=True)
    sold_comment = models.TextField(max_length=400, null=True, blank=True)
    animal_characteristics = models.TextField(max_length=400)
    fur_colour = models.CharField(max_length=100, null=True, blank=True)
    fur_type = models.CharField(max_length=100, null=True, blank=True)
    white_marks = models.BooleanField('Hvide tegn', editable=True, default=False)
    eye_colour = models.CharField(max_length=100, null=True, blank=True)
    male = models.BooleanField('male', editable=True, default=False)
    father = models.ForeignKey('self', related_name='far', on_delete=models.CASCADE, limit_choices_to={'male':True}, null=True, blank=True)
    mother = models.ForeignKey('self', related_name='mor', on_delete=models.CASCADE, limit_choices_to={'male':False}, null=True, blank=True)
    litter = models.ForeignKey('Litter', on_delete=models.CASCADE, null=True, blank=True)
    genotype_a1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_a2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_b1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_b2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_c1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_c2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_d1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_d2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_g1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_g2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_k1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_k2 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_x1 = models.CharField(max_length = 50, null=True, blank=True)
    genotype_x2 = models.CharField(max_length = 50, null=True, blank=True)
    picture = models.ImageField(upload_to='animal_pics', blank=True)
    picture_formatted = models.ImageField(upload_to='animal_pics', blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.animal_name)
        self.slug = slugify(self.animal_name)
        super(Animals, self).save(*args, **kwargs)

    def __str__(self):
        return self.animal_name

    class Meta:
        verbose_name_plural = "Animals"

class Weights(models.Model):
    animals_w = models.ForeignKey(Animals, on_delete=models.CASCADE)
    weight_date = models.DateField('Dato vejet', editable=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        verbose_name_plural = "Weights"

class Comments(models.Model):
    animals = models.ForeignKey(Animals, on_delete=models.CASCADE)
    comments_date = models.DateField(auto_now_add=True)
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

class Litter(models.Model):
    father_l = models.ForeignKey('self', related_name='far_l', on_delete=models.CASCADE, limit_choices_to={'male':True}, null=True, blank=True)
    mother_l = models.ForeignKey('self', related_name='mor_l', on_delete=models.CASCADE, limit_choices_to={'male':False}, null=True, blank=True)
    litter_name = models.CharField('Navn', max_length=200)
    birth_count = models.IntegerField('Antal ved fødsel', default=0)
    litter_characteristics = models.TextField('Kulbeskrivelse', max_length=500)
    born_l = models.DateField('Fødselsdato', editable=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.litter_name)
        self.slug = slugify(self.litter_name)
        super(Litter, self).save(*args, **kwargs)

    def __str__(self):
        return self.litter_name

    class Meta:
        verbose_name_plural = "Litter"

class LitterWeight(models.Model):
    litter_w = models.ForeignKey(Litter, on_delete=models.CASCADE)
    weight_date = models.DateField('Vægtdato', editable=True, blank=True, null=True)
    weight = models.DecimalField('Vægt', max_digits=6, decimal_places=3, default=0)
    number = models.IntegerField('Antal', default=0)

    class Meta:
        verbose_name_plural = "LitterWeight"
