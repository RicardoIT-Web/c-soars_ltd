from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_briefcase, name='view_briefcase')
]
