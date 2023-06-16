from django.urls import path
from my_temp import views

urlpatterns = [
    path('demo_temp/', views.demo_temp, name='demo_temp'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('savedata/', views.savedata, name='savedata'),
    path('displaystudent/', views.displaystudent, name='displaystudent'),
    path('editstudent/<int:dataid>/', views.editstudent, name='editstudent'),
    path('updatestudent/<int:dataid>/', views.updatestudent, name='updatestudent'),
    path('deletestudent/<int:dataid>/', views.deletestudent, name='deletestudent'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('savecourse/', views.savecourse, name='savecourse'),
    path('displaycourse/', views.displaycourse, name='displaycourse'),
    path('editcourse/<int:dataid>/', views.editcourse, name='editcourse'),
    path('updatecourse/<int:dataid>/', views.updatecourse, name='updatecourse'),
    path('deletecourse/<int:dataid>/', views.deletecourse, name='deletecourse'),
    path('log/', views.log, name='log'),
    path('worklogin/', views.worklogin, name='worklogin'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
]