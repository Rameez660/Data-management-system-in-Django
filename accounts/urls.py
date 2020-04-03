from django.urls import path
from . import views
# from django.contrib.auth.views import login

urlpatterns=[

    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customers/<str:pk_test>/', views.customers,name='customers'),
    # path('customers/',views.customers)
    
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('signup/',views.signup,name='signup'),
    path('register_user/',views.register_user,name='register_user'),
    path('login/',views.login,name='login'),
    path('logout/',views.handlelogout,name='handlelogout')
]