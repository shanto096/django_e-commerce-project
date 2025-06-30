from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)] # পণ্যের পরিমাণের জন্য অপশন

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int, # ইন্টিজারে রূপান্তর
                                label='পরিমাণ')
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput) # এই ফিল্ডটি হিডেন থাকবে