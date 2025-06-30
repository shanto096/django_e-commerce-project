from django.db import models
from products.models import Product
from django.conf import settings # AUTH_USER_MODEL পাওয়ার জন্য

# অর্ডার মডেল
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', null=True, blank=True) # অর্ডারকারী ইউজার
    first_name = models.CharField(max_length=50) # প্রথম নাম
    last_name = models.CharField(max_length=50) # শেষ নাম
    email = models.EmailField() # ইমেইল
    address = models.CharField(max_length=250) # ঠিকানা
    postal_code = models.CharField(max_length=20) # পোস্টাল কোড
    city = models.CharField(max_length=100) # শহর
    created = models.DateTimeField(auto_now_add=True) # তৈরির সময়
    updated = models.DateTimeField(auto_now=True) # আপডেটের সময়
    paid = models.BooleanField(default=False) # পেমেন্ট হয়েছে কিনা

    class Meta:
        ordering = ('-created',) # নতুন অর্ডার প্রথমে দেখানোর জন্য

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        # অর্ডারের মোট মূল্য গণনা
        return sum(item.get_cost() for item in self.items.all())

# অর্ডার আইটেম মডেল
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) # অর্ডারের সাথে সম্পর্ক
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE) # পণ্যের সাথে সম্পর্ক
    price = models.DecimalField(max_digits=10, decimal_places=2) # আইটেমের মূল্য (অর্ডার করার সময়কার মূল্য)
    quantity = models.PositiveIntegerField(default=1) # পরিমাণ

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        # একটি আইটেমের মোট মূল্য
        return self.price * self.quantity