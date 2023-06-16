from django.urls import path
from htmlfile import views
urlpatterns = [
    path('facebook/', views.facebook, name="facebook")
]