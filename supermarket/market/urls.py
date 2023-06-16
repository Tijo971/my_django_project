from django.urls import path
from market import views

urlpatterns = [
    path('display/', views.display, name='display')
]