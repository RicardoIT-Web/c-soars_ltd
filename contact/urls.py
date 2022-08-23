""" Contact Us URLs """
from django.urls import path
from . import views
from .views import Inquiries

urlpatterns = [
     path("contact/", views.contact, name="contactUs"),
     path("inquiries/", Inquiries.as_view(), name="inquiries"),
     path("edit_inquiries/<int:inquiries_id>/", views.edit_inquiries, name='edit_inquiries'),
     path("delete_inquiries/<int:inquiries_id>/", views.delete_inquiries, name='delete_inquiries'),
]
