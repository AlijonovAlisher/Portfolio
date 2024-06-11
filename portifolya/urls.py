from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='about'),
    path('single/', single, name='single'),
    path('/works/', works, name='works'),
]
