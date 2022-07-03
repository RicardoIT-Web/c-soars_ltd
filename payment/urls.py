from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment_successful/<order_number>', views.payment_successful,
         name='payment_successful'),
]
