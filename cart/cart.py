from decimal import Decimal
from django.conf import settings
from products.models import Product

# কার্ট ম্যানেজমেন্ট ইউটিলিটি ক্লাস
class Cart:
    def __init__(self, request):
        """
        কার্ট ইনিশিয়ালাইজ করুন।
        """
        self.session = request.session # সেশন অ্যাক্সেস করা
        cart = self.session.get(settings.CART_SESSION_ID) # সেশন থেকে কার্ট ডেটা নেওয়া
        if not cart:
            # যদি কার্ট সেশনে না থাকে, তাহলে একটি খালি কার্ট তৈরি করুন
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        কার্টে একটি পণ্য যোগ করুন অথবা তার পরিমাণ আপডেট করুন।
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save() # সেশনে পরিবর্তন সংরক্ষণ করুন

    def save(self):
        """
        সেশনে কার্ট পরিবর্তনগুলো সংরক্ষণ করুন।
        """
        self.session.modified = True

    def remove(self, product):
        """
        কার্ট থেকে একটি পণ্য সরান।
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        কার্টের আইটেমগুলো পুনরাবৃত্তি করুন এবং ডাটাবেজ থেকে পণ্যগুলো লোড করুন।
        """
        product_ids = self.cart.keys()
        # সংশ্লিষ্ট পণ্য অবজেক্টগুলো পান
        products = Product.objects.filter(id__in=product_ids)

        cart_copy = self.cart.copy() # ইটারেশনের সময় ডিকশনারি পরিবর্তন এড়াতে কপি ব্যবহার করুন
        for product in products:
            cart_copy[str(product.id)]['product'] = product

        for item in cart_copy.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        কার্টের মোট আইটেমের সংখ্যা ফেরত দিন।
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        কার্টের মোট মূল্য ফেরত দিন।
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        কার্ট খালি করুন।
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()