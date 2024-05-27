from django.urls import path
from . import views
urlpatterns = [
    path('',views.signin,name='signin'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('products/',views.products,name='products'),
    path('addproducts/',views.addproducts,name='addproducts'),
    path('viewproduct/<int:product_id>/',views.viewproduct,name='viewproduct'),
    path('editproduct/<int:product_id>/',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:product_id>/',views.deleteproduct,name='deleteproduct'),
    path('logout/', views.UserLogout, name='logout'),

]
