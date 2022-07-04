from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment_successful/<order_number>', views.payment_successful, name='payment_successful'),
    path('cache_payment_data/', views.cache_payment_data, name='cache_payment_data'),
    path('wh/', webhook, name='webhook'),
]
