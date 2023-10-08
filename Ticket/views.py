from django.shortcuts import render, redirect
from .forms import CustomerSupport

def my_view(request):
    if request.method == 'POST':
        form = CustomerSupport(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = CustomerSupport()
    return render(request, 'ticket_template.html', {'form': form})
