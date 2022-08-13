"""Newsletter Models"""
from django.db import models


class Subscriber(models.Model):
    """Model for Subscribers"""
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """Model for issuing newsletters"""
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.subject
