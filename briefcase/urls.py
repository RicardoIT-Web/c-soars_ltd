from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_briefcase, name='view_briefcase'),
    path('add/<item_id>/', views.add_to_briefcase, name='add_to_briefcase'),
]
