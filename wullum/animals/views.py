from django.shortcuts import render
from django.http import HttpResponse

from .models import Animals, FoodPurchases, MiscPurchases, Eggs

# Create your views here.
def index(request):
    animal_list = Animals.objects.order_by('-arrived')

    food_list = FoodPurchases.objects.order_by('-food_date')[:5]

    misc_list = MiscPurchases.objects.order_by('-misc_date')[:5]

    eggs_list = Eggs.objects.order_by('-egg_date')[:7]

    return render(request, 'animals/index.html', {'animal_list': animal_list, 'food_list': food_list, 'misc_list': misc_list, 'eggs_list': eggs_list})
