from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class myAccount(models.Model):
    """
    User account model to retain purchase history and invoice details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.name


@receiver(post_save, sender=User)
def create_update_user_account(sender, instance, created, **kwargs):
    """
    Create/update user account
    """
    if created:
        myAccount.objects.create(user=instance)
    instance.myaccount.save()
