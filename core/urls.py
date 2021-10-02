from django.urls import path, include
from . import views
#from .view import

urlpatterns = [
    path('', views.index, name="index"),
    ]