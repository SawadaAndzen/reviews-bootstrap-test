from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_index, name = "index"),
]