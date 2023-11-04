from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg, CustomerFormReg, CustomerLogin, CustomerSupportLogin, TicketLogin
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .models import CustomerTicket
from Account.models import User


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
            return redirect('customer_support_inquiry')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.support_login, {'form': form, 'error_message': error_message})


def customer_support_inquiry(request):
    return render(request, 'ticket_support_inquiry.html')


class CustomerRegistrationView(View):
    customer_reg = 'ticket_customer_registration.html'
    form_class = CustomerFormReg

    def get(self, request):
        customer = CustomerFormReg()
        return render(request, self.customer_reg, {'form': customer})

    def post(self, request):
        form = CustomerFormReg(request.POST)
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
            return redirect('customer_helpdesk')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.customer_login, {'form': form, 'error_message': error_message})


def customer_helpdesk(request):
    return render(request, 'ticket_customer_helpdesk.html')


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
                return redirect('customer_helpdesk')
            elif user.user_type == 'CS':
                return redirect('customer_support_inquiry')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.template, {'form': form, 'error_message': error_message})


def customer_ticket_history(request):
    return render(request, 'ticket_customer_ticket_history.html')


# saving data in database
def submit_ticket(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        category = request.POST.get('combo')
        description = request.POST.get('message')

        # Check if the username exists in the User model
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Handle the case where the username doesn't exist
            return render(request, 'ticket_login.html', {'message': 'User does not exist'})

        # Create a new CustomerTicket instance and save it to the database
        ticket = CustomerTicket(
            user_id=user,  # Set the user to the retrieved User instance
            ticket_description=description,
            issue_status='O'  # Assuming it's an open issue
        )
        ticket.save()

        # Redirect to a success page or any other page as needed
        return redirect('success_page')

    return render(request, 'ticket_customer_helpdesk.html')


def customer_ticket_history(request):
    # Retrieve CustomerTicket objects
    tickets = CustomerTicket.objects.all()

    # Pass the tickets to the template
    context = {
        'tickets': tickets
    }

    return render(request, 'ticket_customer_ticket_history.html', context)






