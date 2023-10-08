from django.shortcuts import render, redirect
from .forms import CustomerSupportFormReg

def customer_support_registration_view(request):
    if request.method == 'POST':
        form = CustomerSupportFormReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = CustomerSupportFormReg()
    return render(request, 'ticket_template.html', {'form': form})
