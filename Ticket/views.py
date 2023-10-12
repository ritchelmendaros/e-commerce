from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg, CustomerFormReg, CustomerLogin, CustomerSupportLogin, TicketLogin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View


class CustomerSupportRegistrationView(View):
    support_reg = 'ticket_support_registration.html'
    form_class = CustomerSupportFormReg

    def get(self, request):
        customer = CustomerSupportFormReg()
        return render(request, self.support_reg, {'form': customer})

    def post(self, request):
        form = CustomerSupportFormReg(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_type = 'CS'
            user.save()
            login(request, user)
            return redirect('ticket_login')
        return render(request, self.support_reg, {'form': form})


class CustomerSupportLoginView(View):
    support_login = 'ticket_support_login.html'

    def get(self, request):
        form = CustomerSupportLogin()
        return render(request, self.support_login, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('customer_support_index')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.support_login, {'form': form, 'error_message': error_message})


def customer_support_index(request):
    return render(request, 'ticket_support_index.html')


class CustomerRegistrationView(View):
    customer_reg = 'ticket_customer_registration.html'
    form_class = CustomerFormReg

    def get(self, request):
        customer = CustomerFormReg()
        return render(request, self.customer_reg, {'form': customer})

    def post(self, request):
        form = CustomerSupportFormReg(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_type = 'CU'
            user.save()
            login(request, user)
            return redirect('ticket_login')
        return render(request, self.customer_reg, {'form': form})


class CustomerLoginView(View):
    customer_login = 'ticket_customer_login.html'

    def get(self, request):
        form = CustomerLogin()
        return render(request, self.customer_login, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('customer_index')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.customer_login, {'form': form, 'error_message': error_message})


def customer_index(request):
    return render(request, 'ticket_customer_index.html')


class TicketLoginView(View):
    template = 'ticket_login.html'

    def get(self, request):
        form = TicketLogin()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.user_type == 'CU':
                return redirect('customer_index')
            elif user.user_type == 'CS':
                return redirect('customer_support_index')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.template, {'form': form, 'error_message': error_message})






