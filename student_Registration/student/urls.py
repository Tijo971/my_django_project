from django.urls import path
from student import views

urlpatterns=[
    path('stud/', views.stud, name='stud'),
    path('reg/', views.reg, name='reg')
]