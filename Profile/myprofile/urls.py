from django.urls import path
from myprofile import views

urlpatterns = [
        path('profile/', views.profile, name='profile'),
        path('imagefn/', views.imagefn, name='imagefn'),
        path('detailsview/', views.detailsview, name='detailsview'),
        path('savedetails/', views.savedetails, name='savedetails'),
        path('employee/', views.employee, name='employee'),
        path('empdata/',views.empdata, name='empdata')
]