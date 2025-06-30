from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart # কার্ট ইউটিলিটি ক্লাস ইম্পোর্ট
from .forms import CartAddProductForm # কার্ট ফর্ম ইম্পোর্ট

@require_POST # শুধুমাত্র POST রিকোয়েস্ট গ্রহণ করা হবে
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail') # কার্ট ডিটেইল পেজে রিডাইরেক্ট

@require_POST # শুধুমাত্র POST রিকোয়েস্ট গ্রহণ করা হবে
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail') # কার্ট ডিটেইল পেজে রিডাইরেক্ট

def cart_detail(request):
    cart = Cart(request)
    # প্রতিটি কার্ট আইটেমের জন্য আপডেট ফর্ম তৈরি করা
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                            initial={'quantity': item['quantity'],
                                     'override': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})
