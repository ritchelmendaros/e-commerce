from django.db import connection
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomerTicket, TicketCategory
from django.urls import reverse


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
        redirect_url = reverse('customer_ticket_history', kwargs={'username': username})
        return redirect(redirect_url)


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
            redirect_url = reverse('customer_support_inquiry', kwargs={'username': usn})
            return redirect(redirect_url)

        elif result and result[0][0] == 'CU':
            return redirect('customer_helpdesk')

        else:
            msg = 'Unexpected result from the stored procedure'
            return render(request, self.template, {'msg': msg})


class CustomerTicketHistoryView(View):
    template = 'ticket_customer_ticket_history.html'

    def get(self, request, username):
        cursor = connection.cursor()
        args = [username]
        cursor.callproc('DisplayCustomerTicketHistory', args)
        result = cursor.fetchall()
        cursor.close()
        tickets = [{'ticket_id': row[0], 'ticket_description': row[1], 'issue_status': row[2]} for row in result]
        context = {'tickets': tickets, 'username': username}
        return render(request, self.template, context)


class CustomerSupportInquiry(View):
    template = 'ticket_support_inquiry.html'

    def get(self, request, username):
        cursor = connection.cursor()
        cursor.callproc('DisplayCustomerSupportTickets')
        result = cursor.fetchall()
        cursor.close()
        tickets = [{'ticket_id': row[0], 'ticket_description': row[1], 'email': row[2], 'issue_status': row[3]} for row in result]
        context = {'tickets': tickets, 'username': username}
        return render(request, self.template, context)


class CustomerThreadedDiscussionView(View):
    template = 'ticket_customer_thread.html'

    def get(self, request, ticket_id, ticket_description, issue_status, username):
        print(username)
        cursor = connection.cursor()
        args = [username]
        cursor.callproc('GetFirstandLastName', args)
        result = cursor.fetchall()
        cursor.close()

        fullname = result[0][0] if result else 'Default Full Name'

        return render(request, self.template, {
            'ticket_id': ticket_id,
            'ticket_description': ticket_description,
            'issue_status': issue_status,
            'username': username,
            'fullname': fullname,
        })


class SupportThreadedDiscussionView(View):
    template = 'ticket_support_thread.html'

    def get(self, request, ticket_id, ticket_description, email, issue_status):
        cursor = connection.cursor()
        args = [ticket_id]
        cursor.callproc('GetFullNameSupportSide', args)
        result = cursor.fetchall()
        cursor.close()

        fullname = result[0][0] if result else 'Default Full Name'
        print(fullname)

        return render(request, self.template, {
            'ticket_id': ticket_id,
            'ticket_description': ticket_description,
            'issue_status': issue_status,
            'email': email,
            'fullname': fullname,
        })

    def post(self, request):
        replycontent = request.POST['replycontent']
        args = [replycontent]
        cursor.callproc('CheckCredentialsLogin', args)
        result = cursor.fetchall()
        cursor.close()
        if result and 'Incorrect username and password' in result[0]:
            msg = 'Incorrect username and password'
            return render(request, self.template, {'msg': msg})

        elif result and result[0][0] == 'CS':
            redirect_url = reverse('customer_support_inquiry', kwargs={'username': usn})
            return redirect(redirect_url)

        elif result and result[0][0] == 'CU':
            return redirect('customer_helpdesk')

        else:
            msg = 'Unexpected result from the stored procedure'
            return render(request, self.template, {'msg': msg})









