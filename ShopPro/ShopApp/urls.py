from django.urls import path
from ShopApp import views

urlpatterns = [
    path('addshop/',views.addshop, name='addshop'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
    path('prod/', views.prod, name='prod'),
    path('showshop/', views.showshop, name='showshop'),
    path('showproduct/', views.showproduct, name='showproduct'),
    path('editshop/ <int:dataid>/', views.editshop, name='editshop'),
    path('editproduct/ <int:dataid>/', views.editproduct, name='editproduct'),
    path('updateshop/ <int:dataid>/', views.updateshop, name='updateshop'),
    path('updateproduct/ <int:dataid>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/ <int:dataid>/', views.deleteproduct, name='deleteproduct'),
    path('deleteshop/ <int:dataid>/', views.deleteshop, name='deleteshop'),

]