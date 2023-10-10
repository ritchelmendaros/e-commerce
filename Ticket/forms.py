from django.forms import ModelForm
from django import forms
from Account.models import CustomerSupport, User, Customer


class CustomerSupportFormReg(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    mobile_number = forms.CharField(widget=forms.TextInput)
    user_address = forms.CharField(widget=forms.TextInput)
    user_type = forms.ChoiceField(choices=User.type_choices, initial='CS')
    support_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = CustomerSupport
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'mobile_number', 'user_address',
                  'user_type', 'support_name']


class CustomerFormReg(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    mobile_number = forms.CharField(widget=forms.TextInput)
    user_address = forms.CharField(widget=forms.TextInput)
    user_type = forms.ChoiceField(choices=User.type_choices, initial='CU')
    age = forms.IntegerField(widget=forms.NumberInput, initial=0)

    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'mobile_number', 'user_address',
                  'user_type', 'age']

