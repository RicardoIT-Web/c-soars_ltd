""" Contact Us URLs """
from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.ContactFormView.as_view(), name="contact"),
]
