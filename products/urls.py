from django.urls import path
from . import views

app_name = 'products' # অ্যাপ্লিকেশনের নাম

urlpatterns = [
    path('', views.product_list, name='product_list'), # সকল পণ্যের তালিকা
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'), # ক্যাটাগরি অনুযায়ী পণ্যের তালিকা
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'), # পণ্যের বিস্তারিত
]
