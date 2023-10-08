from django.forms import ModelForm
from django import forms
from Account.models import CustomerSupport


class CustomerSupportFormReg(ModelForm):
    user_id = forms.CharField(widget=forms.TextInput)
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    mobile_number = forms.CharField(widget=forms.TextInput)
    address = forms.CharField(widget=forms.TextInput)

    class Meta:
        model=CustomerSupport
        fields=['user_id', 'username','password','email','mobile_number', 'address']

