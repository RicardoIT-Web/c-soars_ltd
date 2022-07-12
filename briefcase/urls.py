""" Briefcase URLs """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_briefcase, name='view_briefcase'),
    path('add/<item_id>/', views.add_to_briefcase, name='add_to_briefcase'),
    path('adjust/<item_id>/', views.adjust_briefcase, name='adjust_briefcase'),
    path('remove/<item_id>/', views.remove_from_briefcase,
         name='remove_from_briefcase'),
]
