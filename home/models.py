""" A model for Users to submit a review of services """

from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class ReviewCard(models.Model):
    """ a model for review cards """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField(max_length=254, blank=True)
    rating = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.service)
