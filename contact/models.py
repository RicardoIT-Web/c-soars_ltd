""" Models for contact us form """
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    This Contact model is to allow Users to reach out to the Restaurant to
    raise any questions or provide any suggests of improvement
    """

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+9999999999'.\
                 Up to 15 digits allowed.",
    )
    contact_number = models.CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True
    )
    subject = models.CharField(blank=True, max_length=100)
    comment = models.CharField(blank=True, max_length=500)
    inquiry_status = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    actioned = models.CharField(max_length=50, default="Open", choices=inquiry_status)

    def __str__(self):
        return self.name
