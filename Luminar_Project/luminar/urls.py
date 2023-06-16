from django.urls import path
from luminar import views

urlpatterns = [
    path('student/', views.student, name='student'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('showstudent/', views.showstudent, name='showstudent'),
]