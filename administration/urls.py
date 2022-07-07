from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('files_list/', views.files_list, name='files_list'),
    path('files_upload/', views.files_upload, name='files_upload'),
]
