""" Contact Us URLs """
from django.urls import path
from . import views
from .views import Inquiries

urlpatterns = [
    path("contact/", views.contact, name="contactUs"),
    path("inquiries/", Inquiries.as_view(), name="inquiries"),
]
