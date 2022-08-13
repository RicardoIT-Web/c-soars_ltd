""" models for payment feature """
import uuid
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from useraccount.models import UserAccount
from services.models import Service


class Order(models.Model):
    """The Order Model retaining User details"""

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_account = models.ForeignKey(
        UserAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=True)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    spotters = models.DecimalField(
        max_digits=6, decimal_places=2, default=150, editable=False
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_briefcase = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default="")

    def _generate_order_number(self):
        """
        Generate an order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a service is added
        """
        self.order_total = (
            self.orderitems.aggregate(Sum("orderitem_total"))[
                "orderitem_total__sum"] or 0
        )
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """A model to retain each order item details"""

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="orderitems",
    )
    service = models.ForeignKey(
        Service, null=False, blank=False, on_delete=models.CASCADE
    )
    FOR = (
        ("Drone Survey with Photos", "Drone Survey with Photos"),
        ("Drone Survey with Video & Photos",
         "Drone Survey with Video & Photos"),
        (
            "Drone Survey with Videos & Photos with Thermal Images",
            "Drone Survey with Videos & Photos with Thermal Images",
        ),
        (
            "Drone Survey Edited Video & Recommendations of Works Required",
            "Drone Survey Edited Video & Recommendations of Works Required",
        ),
        ("Drone Survey with Surveyor Report",
         "Drone Survey with Surveyor Report"),
    )
    description = models.CharField(default=0, max_length=254, choices=FOR)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    spotters = models.DecimalField(max_digits=6, decimal_places=2, default=150)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        """
        self.orderitem_total = self.service.price * self.quantity + self.spotters
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service.name} on order {self.order.order_number}"
