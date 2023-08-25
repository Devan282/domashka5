from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
]


# Create your views here.
