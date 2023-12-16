from django.db import connection
from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg, CustomerFormReg, CustomerLogin, CustomerSupportLogin, TicketLogin
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .models import CustomerTicket, TicketCategory
from Account.models import User
from django.utils import timezone
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.hashers import make_password


class CustomerSupportRegistrationView(View):
    template = 'ticket_support_registration.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        usn = request.POST['username']
        raw_pwd = request.POST['password']
        hashed_pwd = make_password(raw_pwd)
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        number = request.POST['mobile_number']
        address = request.POST['user_address']
        type = 'CS'
        supportname = request.POST['support_name']
        cursor = connection.cursor()
        args = [usn, hashed_pwd, fname, lname, mail, number, address, type, supportname]
        cursor.callproc('InsertNewCS', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Username already exists' in result[0]:
            msg = 'Username already exists'
            return render(request, self.template, {'msg': msg})
        else:
            request.session['username'] = usn
            return redirect('ticket_login')


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


class CustomerRegistrationView(View):
    template = 'ticket_customer_registration.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        usn = request.POST['username']
        raw_pwd = request.POST['password']
        hashed_pwd = make_password(raw_pwd)
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        number = request.POST['mobile_number']
        address = request.POST['user_address']
        type = 'CU'
        user_age = request.POST['age']
        cursor = connection.cursor()
        args = [usn, hashed_pwd, fname, lname, mail, number, address, type, user_age]
        cursor.callproc('InsertNewCU', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Username already exists' in result[0]:
            msg = 'Username already exists'
            return render(request, self.template, {'msg': msg})
        else:
            request.session['username'] = usn
            return redirect('ticket_login')


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
    categories = TicketCategory.CATEGORY_CHOICES  # Get the category choices
    context = {
        'categories': categories,
    }
    return render(request, 'ticket_customer_helpdesk.html', context)


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


# saving data in database
def submit_ticket(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        category_name = request.POST.get('category_name')
        description = request.POST.get('message')

        print("Received username:", username)

        try:
            user = User.objects.get(username=username)
            print("Found user:", user)
        except User.DoesNotExist:
            print("User does not exist")
            return HttpResponseNotFound('User does not exist')
        # Create a new CustomerTicket instance and save it to the database
        ticket = CustomerTicket(
            user_id=user,
            ticket_description=description,
            ticket_date=timezone.now(),
            issue_status='O'
        )
        ticket.save()
        # Create a new TicketCategory instance and save it to the database
        if category_name:
            ticket_category = TicketCategory(
                ticket_id=ticket,
                category_name=category_name
            )
            ticket_category.save()
        else:
            # Handle the case where category_name is empty (null)
            return HttpResponse('Category name cannot be empty', status=400)
        # Redirect to a success page or any other page as needed
        return redirect('customer_ticket_history')
    return render(request, 'ticket_customer_helpdesk.html')


def customer_ticket_history(request):
    tickets = CustomerTicket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'ticket_customer_ticket_history.html', context)


def customer_support_inquiry(request):
    tickets = CustomerTicket.objects.all()
    context = {
        'tickets': tickets
    }

    return render(request, 'ticket_support_inquiry.html', context)







