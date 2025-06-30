# myecommerceproject/core/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# আপনার কাস্টম ইউজার মডেলের জন্য একটি কাস্টম রেজিস্ট্রেশন ফর্ম
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # এটি আপনার settings.py তে সেট করা AUTH_USER_MODEL ব্যবহার করবে
        fields = UserCreationForm.Meta.fields # ইউজারনেম এবং পাসওয়ার্ড ফিল্ডগুলো ব্যবহার করবে
