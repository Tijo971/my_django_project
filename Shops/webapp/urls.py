from django.urls import path
from webapp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/<cat_nme>', views.products, name='products'),
    path('singlepdt/<int:dataid>/', views.singlepdt, name='singlepdt'),
    path('', views.userlogin, name='userlogin'),
    path('usersignin/', views.usersignin, name='usersignin'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('userloginprocess/', views.userloginprocess, name='userloginprocess'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('savecontacts/', views.savecontacts, name='savecontacts'),

]