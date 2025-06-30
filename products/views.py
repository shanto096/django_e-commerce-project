from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm # কার্টে যোগ করার ফর্ম ইম্পোর্ট করা হয়েছে

# পণ্যের তালিকা দেখানোর ভিউ
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all() # সকল ক্যাটাগরি
    products = Product.objects.filter(available=True) # উপলব্ধ সকল পণ্য
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) # নির্বাচিত ক্যাটাগরির পণ্য

    return render(request, 'products/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# পণ্যের বিস্তারিত তথ্য দেখানোর ভিউ
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True) # নির্দিষ্ট পণ্য
    cart_product_form = CartAddProductForm() # কার্টে যোগ করার ফর্ম
    return render(request, 'products/product_detail.html', {
        'product': product,
        'cart_product_form': cart_product_form
    })