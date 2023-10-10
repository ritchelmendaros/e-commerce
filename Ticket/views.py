from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg, CustomerFormReg
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def customer_support_registration_view(request):
    if request.method == 'POST':
        form = CustomerSupportFormReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_support_login')
    else:
        form = CustomerSupportFormReg()
    return render(request, 'ticket_support_registration.html', {'form': form})


def customer_support_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_support_index')
    else:
        form = AuthenticationForm()

    return render(request, 'ticket_support_login.html', {'form': form})


def customer_support_index(request):
    return render(request, 'ticket_support_index.html')


def customer_registration_view(request):
    if request.method == 'POST':
        form = CustomerFormReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_support_login')
    else:
        form = CustomerFormReg()
    return render(request, 'ticket_customer_registration.html', {'form': form})


def customer_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_index')
    else:
        form = AuthenticationForm()

    return render(request, 'ticket_customer_login.html', {'form': form})


def customer_index(request):
    return render(request, 'ticket_customer_index.html')
