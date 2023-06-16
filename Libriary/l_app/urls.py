from django.urls import path
from l_app import views

urlpatterns=[
    path('mybook/', views.mybook, name='mybook'),
    path('savedata/', views.savedata, name='savedata'),
    path('myuser/', views.myuser, name='myuser'),
    path('saveuser/', views.saveuser, name='saveuser')
]