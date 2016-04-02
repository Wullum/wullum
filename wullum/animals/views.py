from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone

from .forms import AddAnimal, AddComment
from .models import Animals, FoodPurchases, MiscPurchases, Eggs, Comments


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

    one_animal = get_object_or_404(Animals, slug=animal_name_slug)

    comment_list = Comments.objects.order_by('-comments_date')

    if request.method == "POST":
        form = AddComment(request.POST)

        if form.is_valid():
            form.animals = Animals.objects.get(slug=animal_name_slug)
            form.comment_date = timezone.now()
            form.save(commit=True)

            return HttpResponseRedirect('/animals')

        else:
            print(form.errors)

    else:
        form = AddComment

    return render(request, 'animals/animal.html', {'one_animal': one_animal, 'form': form, 'comment_list': comment_list})
