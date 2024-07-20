from django.urls import path
from . import views

app_name = 'ecomapp'

urlpatterns = [
    path('', views.main, name='main'),
]
