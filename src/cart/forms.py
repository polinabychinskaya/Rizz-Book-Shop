from django import forms
from . import models
class CreateOrderForm(forms.Form):
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput
    )

    CHOICES = (('Cash on delivery', 'Cash on delivery'),('E-wallet', 'E-wallet'),('Credit or debit cards', 'Credit or debit cards'),('Mobile payment', 'Mobile payment'))
    payment_method = forms.ChoiceField(
        required=True,
        choices=CHOICES)

    address = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

