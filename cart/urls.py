from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'), # কার্ট ডিটেইল
    path('add/<int:product_id>/', views.cart_add, name='cart_add'), # কার্টে পণ্য যোগ
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'), # কার্ট থেকে পণ্য সরান
]