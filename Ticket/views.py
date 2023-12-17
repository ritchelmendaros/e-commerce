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
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        number = request.POST['mobile_number']
        address = request.POST['user_address']
        type = 'CS'
        supportname = request.POST['support_name']
        cursor = connection.cursor()
        args = [usn, raw_pwd, fname, lname, mail, number, address, type, supportname]
        cursor.callproc('InsertNewCS', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Username already exists' in result[0]:
            msg = 'Username already exists'
            return render(request, self.template, {'msg': msg})
        else:
            request.session['username'] = usn
            return redirect('ticket_login')


class CustomerRegistrationView(View):
    template = 'ticket_customer_registration.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        usn = request.POST['username']
        raw_pwd = request.POST['password']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        number = request.POST['mobile_number']
        address = request.POST['user_address']
        type = 'CU'
        user_age = request.POST['age']
        cursor = connection.cursor()
        args = [usn, raw_pwd, fname, lname, mail, number, address, type, user_age]
        cursor.callproc('InsertNewCU', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Username already exists' in result[0]:
            msg = 'Username already exists'
            return render(request, self.template, {'msg': msg})
        else:
            request.session['username'] = usn
            return redirect('ticket_login')


class CustomerHelpdeskView(View):
    template = 'ticket_customer_helpdesk.html'

    def get(self, request):
        cursor = connection.cursor()
        query ='select * from DisplayCategory'
        cursor.execute(query)
        categories = cursor.fetchall()
        cursor.close()
        msg = categories
        return render(request, self.template, {'msg': msg})

    def post(self, request):
        username = request.POST.get('username')
        category_name = request.POST.get('category_name')
        description = request.POST.get('message')
        cursor = connection.cursor()
        args = [username, category_name, description]
        cursor.callproc('InsertNewTicket', args)
        result = cursor.fetchall()
        cursor.close()
        return redirect('customer_ticket_history')


class TicketLoginView(View):
    template = 'ticket_login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        usn = request.POST['username']
        pwd = request.POST['password']
        cursor = connection.cursor()
        args = [usn, pwd]
        cursor.callproc('CheckCredentialsLogin', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Incorrect username and password' in result[0]:
            msg = 'Incorrect username and password'
            return render(request, self.template, {'msg': msg})

        elif result and result[0][0] == 'CS':
            msg = 'CS'
            return render(request, self.template, {'msg': msg})

        elif result and result[0][0] == 'CU':
            msg = 'CU'
            return redirect('customer_helpdesk')

        else:
            msg = 'Unexpected result from the stored procedure'
            return render(request, self.template, {'msg': msg})


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









