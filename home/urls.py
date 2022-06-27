from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user_review/<int:service_name>/', views.user_review, name='user_review')
]
