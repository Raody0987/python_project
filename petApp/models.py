from django.db import models

# Create your models here.
#pet adoption project => Pet, Vaccines (many -to- many)


class Vaccine(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name
class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    submitter = models.CharField(max_length= 155)
    age = models.IntegerField(blank=True)
    description = models.TextField(blank=True, null=True)
    Vaccine = models.ManyToManyField(Vaccine)

    def __str__(self):
        return self.name

    