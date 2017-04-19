# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import AddAnimal, AddComment, AddWeight, KillAnimal, RemoveAnimal, AddRabbit, AddChicken, AddGoat
from .models import Animals, FoodPurchases, MiscPurchases, Eggs, Comments, Weights, UserProfile


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

    return render(request, 'animals/all.html', {'animal_list': animal_list})

@login_required
def add_all(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            form = AddAnimal(request.POST, request.FILES)
            if form.is_valid():
                animal = form.save(commit=False)
                if 'picture' in request.FILES:
                    animal.picture = request.FILES['picture']

                animal.save()

                return index(request)
            else:
                print(form.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    else:
        form = AddAnimal()

    return render(request, 'animals/add.html', {'form':form})


def animal(request, animal_name_slug):

    one_animal = get_object_or_404(Animals, slug=animal_name_slug)

    comment_list = Comments.objects.filter(animals_id=one_animal.id).order_by('-comments_date', '-id')

    weight_list = Weights.objects.filter(animals_w_id=one_animal.id).order_by('-weight_date', '-id')

    id_animal = Animals.objects.get(slug=animal_name_slug)

    if request.method == "POST" and "submit_comment" in request.POST:
        form = AddComment(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.animals = id_animal
                form.save(commit=True)

                return HttpResponseRedirect('')

            else:
                print(form.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    elif request.method == "POST" and "submit_weight" in request.POST:
        form_w = AddWeight(request.POST)

        if request.user.is_authenticated:
            if form_w.is_valid():
                weight = form_w.save(commit=False)
                weight.animals_w = id_animal
                form_w.save(commit=True)

                return HttpResponseRedirect('')

            else:
                print(form_w.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    elif request.method == "POST" and "submit_kill" in request.POST:
        form_a = KillAnimal(request.POST, instance=one_animal)

        if request.user.is_authenticated:
            if form_a.is_valid():
                form_a.save()

                return HttpResponseRedirect('/animals/dead')

            else:
                print(form_a.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    elif request.method == "POST" and "submit_gone" in request.POST:
        form_g = RemoveAnimal(request.POST, instance=one_animal)

        if request.user.is_authenticated:
            if form_g.is_valid():
                form_g.save()

                return HttpResponseRedirect('/animals')
            else:
                print(form_g.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    else:
        form_w = AddWeight()
        form_a = KillAnimal()
        form = AddComment()
        form_g = RemoveAnimal()


    return render(request, 'animals/animal.html', {'one_animal': one_animal, 'form_a': form_a, 'form_g': form_g,
                        'form': form, 'form_w': form_w, 'comment_list': comment_list, 'weight_list': weight_list})

def dead(request):
    animal_list = Animals.objects.filter(dead=True).exclude(gone=True).order_by('-departure')

    kill_count = Animals.objects.filter(dead=True).count()

    return render(request, 'animals/dead.html', {'animal_list': animal_list, 'kill_count':kill_count})

def rabbits(request):
    animal_list = Animals.objects.filter(species='Kanin').exclude(dead=True).exclude(gone=True).order_by('-arrived')

    return render(request, 'animals/rabbits.html', {'animal_list': animal_list})

@login_required
def add_rabbit(request):
    if request.method == 'POST':
        form = AddRabbit(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                animal = form.save(commit=False)
                if 'picture' in request.FILES:
                    animal.picture = request.FILES['picture']

                animal.save()

                return HttpResponseRedirect('/animals/rabbits')

            else:
                print(form.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    else:
        form = AddRabbit()

    return render(request, 'animals/add_rabbit.html', {'form': form})

def chickens(request):
    chicken_list = Animals.objects.filter(species='Høne').exclude(dead=True).exclude(gone=True).order_by('-arrived')
    cock_list = Animals.objects.filter(species='Hane').exclude(dead=True).exclude(gone=True).order_by('-arrived')

    return render(request, 'animals/chickens.html', {'chicken_list': chicken_list, 'cock_list': cock_list})

@login_required
def add_chicken(request):
    if request.method == 'POST':
        form = AddChicken(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                animal = form.save(commit=False)
                if 'picture' in request.FILES:
                    animal.picture = request.FILES['picture']

                animal.save()

                return HttpResponseRedirect('')

            else:
                print(form.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    else:
        form = AddChicken()

    return render(request, 'animals/add_chicken.html', {'form':form})

def goats(request):
    animal_list = Animals.objects.filter(species='Ged').order_by('-arrived')

    return render(request, 'animals/goats.html', {'animal_list': animal_list})

@login_required
def add_goat(request):
    if request.method == 'POST':
        form = AddGoat(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                animal = form.save(commit=False)
                if 'picture' in request.FILES:
                    animal.picture = request.FILES['picture']

                animal.save()

                return HttpResponseRedirect('')
            else:
                print(form.errors)
        else:
            return HttpResponseRedirect('/animals/login')

    else:
        form = AddGoat()

    return render(request, 'animals/add_goat.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/animals')
            else:
                return HttpResponse("Din kono er ikke aktiv")
        else:
            print("Invalid login details: {0},{1}".format(username, password))
            return HttpResponse("Ugyldig login")
    else:
        return render(request, 'animals/login.html')

@login_required
def user_logout(request):
    logout(request)

    return index(request)