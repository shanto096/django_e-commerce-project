from django.db import models
from django.contrib.auth.models import AbstractUser

# কাস্টম ইউজার মডেল। আপনি চাইলে এখানে অতিরিক্ত ফিল্ড যোগ করতে পারেন।
# এই প্রজেক্টে ডিফল্ট AbstractUser ব্যবহার করা হয়েছে।
class CustomUser(AbstractUser):
    # উদাহরণ: phone_number = models.CharField(max_length=15, blank=True, null=True)
    pass