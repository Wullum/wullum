from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import AddAnimal, AddComment, AddWeight, KillAnimal, RemoveAnimal
from .models import Animals, FoodPurchases, MiscPurchases, Eggs, Comments, Weights


# Create your views here.
def index(request):
    animal_list = Animals.objects.exclude(dead=True).exclude(gone=True).order_by('species', '-arrived')

    kill_count = Animals.objects.filter(dead=True).count()

    food_list = FoodPurchases.objects.order_by('-food_date')[:5]

    misc_list = MiscPurchases.objects.order_by('-misc_date')[:5]

    eggs_list = Eggs.objects.order_by('-egg_date')[:7]

    return render(request, 'animals/index.html', {'animal_list': animal_list, 'kill_count': kill_count,
            'food_list': food_list, 'misc_list': misc_list, 'eggs_list': eggs_list})


def all(request):
    animal_list = Animals.objects.exclude(dead=True).order_by('-arrived')

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

    comment_list = Comments.objects.filter(animals_id=one_animal.id).order_by('-comments_date', '-id')

    weight_list = Weights.objects.filter(animals_w_id=one_animal.id).order_by('-weight_date', '-id')

    id_animal = Animals.objects.get(slug=animal_name_slug)

    if request.method == "POST" and "submit_comment" in request.POST:
        form = AddComment(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.animals = id_animal
            form.save(commit=True)

            return HttpResponseRedirect('')

        else:
            print(form.errors)

    elif request.method == "POST" and "submit_weight" in request.POST:
        form_w = AddWeight(request.POST)

        if form_w.is_valid():
            weight = form_w.save(commit=False)
            weight.animals_w = id_animal
            form_w.save(commit=True)

            return HttpResponseRedirect('')

        else:
            print(form_w.errors)

    elif request.method == "POST" and "submit_kill" in request.POST:
        form_a = KillAnimal(request.POST, instance=one_animal)

        if form_a.is_valid():
            form_a.save()

            return HttpResponseRedirect('/animals/dead')

        else:
            print(form_a.errors)

    elif request.method == "POST" and "submit_gone" in request.POST:
        form_g = RemoveAnimal(request.POST, instance=one_animal)

        if form_g.is_valid():
            form_g.save()

            return HttpResponseRedirect('/animals')
        else:
            print(form_g.errors)

    else:
        form_w = AddWeight
        form_a = KillAnimal
        form = AddComment
        form_g = RemoveAnimal


    return render(request, 'animals/animal.html', {'one_animal': one_animal, 'form_a': form_a, 'form_g': form_g,
                        'form': form, 'form_w': form_w, 'comment_list': comment_list, 'weight_list': weight_list})

def dead(request):
    animal_list = Animals.objects.filter(dead=True).exclude(gone=True).order_by('-departure')

    kill_count = Animals.objects.filter(dead=True).count()

    return render(request, 'animals/dead.html', {'animal_list': animal_list, 'kill_count':kill_count})
