from django.shortcuts import render
from django.http import HttpResponse

from .models import Animals

# Create your views here.
def index(request):
    animal_list = Animals.objects.order_by('-arrived')
    animals = {'animal_list': animal_list}
    return render(request, 'animals/index.html', animals)
