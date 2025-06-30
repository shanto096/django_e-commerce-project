# myecommerceproject/orders/views.py
from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart # কার্ট ইম্পোর্ট

# অর্ডার তৈরির ভিউ
def order_create(request):
    cart = Cart(request) # সেশন থেকে কার্ট লোড
    if request.method == 'POST':
        form = OrderCreateForm(request.POST) # ফর্ম ডেটা
        if form.is_valid():
            order = form.save(commit=False) # অর্ডার অবজেক্ট তৈরি কিন্তু সেভ না করে
            if request.user.is_authenticated: # যদি ইউজার লগইন করা থাকে
                order.user = request.user
            order.save() # অর্ডার সেভ করা

            # কার্টের প্রতিটি আইটেম থেকে OrderItem তৈরি করা
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear() # অর্ডার সফল হলে কার্ট খালি করুন

            # পেমেন্ট বা ধন্যবাদ পেজে রিডাইরেক্ট করুন
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm() # খালি ফর্ম
    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'form': form
    })