from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserAccount(models.Model):
    """
    User account model for retaining historical purchases and
    invoice details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update_account(sender, instance, created, **kwargs):
    """
    create/updte user account
    """
    if created:
        UserAccount.objects.create(user=instance)
    instance.UserAccount.save()
