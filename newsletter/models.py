from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.subject
