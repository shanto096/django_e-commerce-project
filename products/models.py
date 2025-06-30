from django.db import models
from django.urls import reverse

# ক্যাটাগরি মডেল
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # ক্যাটাগরির নাম
    slug = models.SlugField(unique=True) # URL এর জন্য স্ল্যাগ

    class Meta:
        ordering = ('name',) # নামের ভিত্তিতে সাজানো হবে
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

# প্রোডাক্ট মডেল
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # ক্যাটাগরির সাথে সম্পর্ক
    name = models.CharField(max_length=200) # পণ্যের নাম
    slug = models.SlugField(unique=True) # URL এর জন্য স্ল্যাগ
    description = models.TextField() # পণ্যের বিবরণ
    price = models.DecimalField(max_digits=10, decimal_places=2) # পণ্যের মূল্য
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True) # পণ্যের ছবি
    stock = models.PositiveIntegerField() # স্টকের পরিমাণ
    available = models.BooleanField(default=True) # পণ্য উপলব্ধ কিনা
    created_at = models.DateTimeField(auto_now_add=True) # তৈরির সময়
    updated_at = models.DateTimeField(auto_now=True) # আপডেটের সময়

    class Meta:
        ordering = ('name',) # নামের ভিত্তিতে সাজানো হবে
        index_together = (('id', 'slug'),) # দ্রুত কোয়েরির জন্য ইনডেক্স

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])
