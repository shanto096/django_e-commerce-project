from .cart import Cart

# এটি প্রতিটি রিকোয়েস্টে কার্ট অবজেক্টকে টেমপ্লেট কন্টাক্সটে উপলব্ধ করবে।
def cart(request):
    return {'cart': Cart(request)}