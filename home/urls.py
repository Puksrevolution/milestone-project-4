"""
Code adapted from the CI Boutique Ado mini project
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home')
]
