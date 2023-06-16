from django.urls import path
from student_app import views

urlpatterns=[
    path('student/',views.student, name='student'),
    path('savedata/',views.savedata, name='savedata')
]