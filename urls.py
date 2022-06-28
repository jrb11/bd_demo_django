from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('user_details_registration/', views.user_details_registration, name='user_details_registration'),
    path('user_details_view/', views.user_details_view, name='user_details_view'),
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('product_registration/', views.product_registration, name='product_registration'),
    path('seller_product_view/', views.seller_product_view, name='seller_product_view'),
    path('buyer_product_view/', views.buyer_product_view, name='buyer_product_view'),
    path('buy_product/<int:pk>',views.buy_product, name="buy_product"),
    path('user_purchase/', views.user_purchase, name='user_purchase'),
    path('order_history/',views.order_history, name='order_history'),
]   
