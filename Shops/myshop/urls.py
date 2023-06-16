from django.urls import path
from myshop import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('save_category/', views.save_category, name='save_category'),
    path('disp_category/', views.disp_category, name='disp_category'),
    path('edit_category/<int:dataid>/', views.edit_category, name='edit_category'),
    path('updatae_category/<int:dataid>/', views.updatae_category, name='updatae_category'),
    path('delete_category/<int:dataid>/', views.delete_category, name='delete_category'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('saveproduct/', views.saveproduct, name='saveproduct'),
    path('display_product/', views.display_product, name='display_product'),
    path('delete_product/<int:dataid>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:dataid>/', views.edit_product, name='edit_product'),
    path('update_product/<int:dataid>/', views.update_product, name='update_product'),
    path('', views.loginpage, name='loginpage'),
    path('loginprocess/', views.loginprocess, name='loginprocess'),
    path('logout/', views.logout, name='logout'),
    path('displaycontacts/', views.displaycontacts, name='displaycontacts'),
    path('deletecontact/<int:dataid>', views.deletecontact, name='deletecontact'),
]