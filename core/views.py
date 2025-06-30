from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

# হোম পেজ ভিউ
def home_view(request):
    return render(request, 'home.html')

# রেজিস্ট্রেশন ভিউ
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # সফল রেজিস্ট্রেশনের পর লগইন পেজে রিডাইরেক্ট
    template_name = 'registration/register.html'