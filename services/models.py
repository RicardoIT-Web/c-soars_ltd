""" Service app models for retaining services data """
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Categorizing services models """
    class Meta:
        """ pluralize model title """
        verbose_name_plural = 'Categories'

    TYPES = (
        ('Civil Engineering Structures', 'Civil Engineering Structures'),
        ('External Fire Risk Inspections', 'External Fire Risk Inspections'),
        ('Domestic & Commercial Surveys - Chimney & Roof Inspections',
         'Domestic & Commercial Surveys - Chimney & Roof Inspections'),
        ('Domestic & Commercial Surveys - Roof Inspections All Areas',
         'Domestic & Commercial Surveys - Roof Inspections All Areas'),
        ('Domestic & Commercial Surveys - Gutter & Roof Inspections',
         'Domestic & Commercial Surveys - Gutter & Roof Inspections'),
        ('Domestic & Commercial Surveys - Dangerous Structures Inspections',
         'Domestic & Commercial Surveys - Dangerous Structures Inspections'),
    )
    name = models.CharField(max_length=254, choices=TYPES)

    FN_TYPES = (
        ('CES', 'CES'),
        ('EFRI', 'EFRI'),
        ('D&CS I', 'D&CS I'),
        ('D&CS II', 'D&CS II'),
        ('D&CS III', 'D&CS III'),
        ('D&CS IV', 'D&CS IV'),
    )
    friendly_name = models.CharField(max_length=50, choices=FN_TYPES)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ display friendly name """
        return self.friendly_name


class Service(models.Model):
    """ Services Model for retaining  services data """
    class Meta:
        """ Pluralize service model """
        verbose_name_plural = 'Services'

    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    TYPES = (
        ('Civil Engineering Structures', 'CES'),
        ('External Fire Risk Inspections', 'EFRI'),
        ('Domestic & Commercial Surveys - Chimney & Roof Inspections',
         'D&CS I'),
        ('Domestic & Commercial Surveys - Roof Inspections All Areas',
         'D&CS II'),
        ('Domestic & Commercial Surveys - Gutter & Roof Inspections',
         'D&CS III'),
        ('Domestic & Commercial Surveys - Dangerous Structures Inspections',
         'D&CS IV'),
    )
    name = models.CharField(max_length=254, choices=TYPES)

    FOR = (
        ('Drone Survey with Photos', 'Drone Survey with Photos'),
        ('Drone Survey with Video & Photos',
         'Drone Survey with Video & Photos'),
        ('Drone Survey with Videos & Photos with Thermal Images',
         'Drone Survey with Videos & Photos with Thermal Images'),
        ('Drone Survey Edited Video & Recommendations of Works Required',
         'Drone Survey Edited Video & Recommendations of Works Required'),
        ('Drone Survey with Surveyor Report',
         'Drone Survey with Surveyor Report'),
    )
    description = models.CharField(max_length=254, choices=FOR)
    OPTIONS = (
        ('Pre-site Survey & Risk Assessment, Drone Survey of Intended Area\
            & Photos', 'Pre-site Survey & Risk Assessment, \
            Drone Survey of Intended Area & Photos'),
        ('Pre-site Survey & Risk Assessment, Drone Survey of Intended Area,\
            Videos & Photos', 'Pre-site Survey & Risk Assessment,\
            Drone Survey of Intended Area, Videos & Photos'),
        ('Pre-site Survey & Risk Assessment, Drone Survey of Intended Area,\
            Videos, Photos & Thermal Imaging', 'Pre-site Survey & Risk\
                Assessment, Drone Survey of Intended Area,\
                Videos, Photos & Thermal Imaging'),
        ('Pre-site Survey & Risk Assessment, Drone Survey of Intended Area,\
            Edited Video Presentation & Recommendations of Works Required',
            'Pre-site Survey & Risk Assessment, Drone Survey of Intended Area,\
            Edited Video Presentation & Recommendations of Works Required'),
        ('Pre-site Survey & Risk Assessment, Drone Survey of Intended Area\
             & Surveyor Report', 'Pre-site Survey & Risk Assessment,\
                Drone Survey of Intended Area & Surveyor Report'),
    )
    includes = models.CharField(max_length=254, choices=OPTIONS)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    spotters = models.DecimalField(max_digits=6, decimal_places=2, default=150)
    images = models.ImageField(default='noimage.png', blank=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    comment = models.TextField(blank=True)
    STATUS = (
        ('Started', 'Started'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=10, default="Started", choices=STATUS)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        """ display total price(sum of price + spotters) """
        return self.price + self.spotters
