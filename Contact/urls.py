from django.urls import path
from . import views
from Contact import views

urlpatterns = [
    path('', views.Contact, name='Contact'),
]
