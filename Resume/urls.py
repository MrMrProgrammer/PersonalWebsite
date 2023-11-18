from django.urls import path
from . import views

urlpatterns = [
    path('', views.Resume, name='Resume'),
]
