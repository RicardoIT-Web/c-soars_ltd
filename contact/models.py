from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Contact(models.Model):
    '''
    This Contact model is to allow Users to reach out to the Restaurant to
    raise any questions or provide any suggests of improvement
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    subject = models.CharField(blank=True, max_length=100)
    comment = models.CharField(blank=True, max_length=500)
    actioned = models.BooleanField(default=False)
