from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_view # হোম ভিউ ইম্পোর্ট করা হয়েছে

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # হোম পেজ
    path('accounts/', include('django.contrib.auth.urls')), # Django'র বিল্ট-ইন অথেন্টিকেশন URLs
    path('accounts/', include('core.urls')), # আপনার কাস্টম অথেন্টিকেশন URLs (যেমন রেজিস্ট্রেশন)
    path('products/', include('products.urls', namespace='products')), # পণ্য সম্পর্কিত URLs
    path('cart/', include('cart.urls', namespace='cart')), # কার্ট সম্পর্কিত URLs
    path('orders/', include('orders.urls', namespace='orders')), # অর্ডার সম্পর্কিত URLs
]

# ডেভেলপমেন্টের জন্য মিডিয়া ফাইল সার্ভ করা
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
