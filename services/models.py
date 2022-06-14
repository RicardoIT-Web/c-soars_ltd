from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    TYPES = (
        ('Civil Engineering Structures', 'CES'),
        ('External Fire Risk Inspections', 'EFRI'),
        ('Domestic & Commercial Surveys', 'D&CS'),
    )
    name = models.CharField(max_length=50, choices=TYPES)
    FOR = (
        ('Drone survey with photos', 'Drone survey with photos'),
        ('Drone survey with Video & photos', 'Drone survey with Video & photos'),
        ('Drone survey with videos & photos with thermal images', 'Drone survey with videos & photos with thermal images'),
        ('Drone survey edited version & recommendations of work', 'Drone survey edited version & recommendations of work'),
        ('Drone survey with surveyor report', 'Drone survey with surveyor report'),
    )
    includes = models.CharField(max_length=100, choices=FOR)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    spotters = models.DecimalField(max_digits=6, decimal_places=2, default=150)

    def __str__(self):
        return self.name
