from django.urls import path
from . import views
from Nitto1.views import shoeInfo

urlpatterns = [
    path('', views.inherit, name='inherit'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.theLogin, name='login'),
    path('logout/', views.logOutUser, name='logout'),
    path('pannelInherit/', views.pannelInherit, name='pannelInherit'),
    path('adminProf/', views.adminProf, name='adminProf'),
    path('allCustomers/', views.allCustomers, name='allCustomers'),
    path('delCustomer/<str:username>/',views.delCustomer, name='delCustomer'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('allProducts/', views.allProducts, name='allProducts'),
    path('delProduct/<str:pk>/', views.delProduct, name='delProduct'),
    path('shoeInfo/<str:pk>/', shoeInfo.as_view(), name='shoeInfo'),
]