from django.shortcuts import render
from .models import Vaccine, Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all() #sellect all from pet table

    return render(request, 'home.html', {'pets': pets})

def pet_details(request, id):
    specific_pet = Pet.objects.get(pk=id)
    return render(request, 'details.html', {'pet_details': specific_pet})
   