from django.shortcuts import render, redirect
from .forms import CustomerSupportForm


def CustomerSupportView(request):
    if request.method == 'POST':
        form = CustomerSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = CustomerSupportForm()
    return render(request, 'ticket_template.html', {'form': form})
