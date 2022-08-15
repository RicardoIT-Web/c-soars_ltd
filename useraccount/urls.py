""" User Account URLs """
from django.urls import path
from . import views
from .views import Reviews

urlpatterns = [
    path("", views.useraccount, name="useraccount"),
    path(
        "purchase_history/<order_number>",
        views.purchase_history,
        name="purchase_history",
    ),
    path("submit_review/<service_id>", views.submit_review, name="submit_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
]
