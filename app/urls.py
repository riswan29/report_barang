from django.urls import path, include
from .views import *


urlpatterns = [
    path('', search_progress, name='search_progress'),
]
