from django.shortcuts import render
from django.http import HttpResponse

from .models import Animals, FoodPurchases, MiscPurchases, Eggs
from .forms import AddAnimal


# Create your views here.
def index(request):
    animal_list = Animals.objects.order_by('-arrived')

    food_list = FoodPurchases.objects.order_by('-food_date')[:5]

    misc_list = MiscPurchases.objects.order_by('-misc_date')[:5]

    eggs_list = Eggs.objects.order_by('-egg_date')[:7]

    return render(request, 'animals/index.html',
                  {'animal_list': animal_list, 'food_list': food_list, 'misc_list': misc_list, 'eggs_list': eggs_list})


def all(request):
    animal_list = Animals.objects.order_by('-arrived')

    if request.method == 'POST':
        form = AddAnimal(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print(form.errors)

    else:
        form = AddAnimal()

    return render(request, 'animals/all.html', {'animal_list': animal_list, 'form': form})


def animal(request, animal_name_slug):
    context_dict = {}

    try:
        animal = Animals.objects.get(slug=animal_name_slug)
        context_dict['animal_name'] = animal.animal_name

    except Animals.DoesNotExist:
        pass

    return render(request, 'animals/animal.html', context_dict)
