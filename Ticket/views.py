from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def customer_support_registration_view(request):
    if request.method == 'POST':
        form = CustomerSupportFormReg(request.POST)
        if form.is_valid():
            customer_support = form.save(commit=False)
            customer_support.address = form.cleaned_data['address']
            customer_support.save()
            return redirect('customer_support_login')
    else:
        form = CustomerSupportFormReg()
    return render(request, 'ticket_registration.html', {'form': form})


def customer_support_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to the profile page or another desired page
    else:
        form = AuthenticationForm()

    return render(request, 'ticket_login.html', {'form': form})
