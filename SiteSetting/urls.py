from django.urls import path
from . import views
from Contact.views import get_message

urlpatterns = [
    path('', views.Home, name='Home'),

    path('Resume', views.Resume, name='Resume'),

    path('Projects', views.Projects, name='Projects'),

    path('Contact', get_message, name='Contact'),
]
