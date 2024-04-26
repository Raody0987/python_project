from django.contrib import admin
from .models import Vaccine, Pet

# Register your models here.
admin.site.register(Vaccine)
#admin.site.register(Pet)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'species','breed', 'gender', 'age','submitter'
    )
