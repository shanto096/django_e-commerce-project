# myecommerceproject/core/views.py
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # এই লাইনটি আর লাগবে না
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm # আপনার নতুন কাস্টম ফর্ম ইম্পোর্ট করা হয়েছে

# হোম পেজ ভিউ
def home_view(request):
    return render(request, 'home.html')

# রেজিস্ট্রেশন ভিউ
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm # এখানে আপনার কাস্টম ফর্ম ব্যবহার করা হয়েছে
    success_url = reverse_lazy('login') # সফল রেজিস্ট্রেশনের পর লগইন পেজে রিডাইরেক্ট
    template_name = 'registration/register.html'

