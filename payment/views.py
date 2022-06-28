from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm



def payment(request):
    briefcase = request.session.get('briefcase', {})
    if not briefcase:
        messages.error(request, "Your Briefcase is currently empty")
        return redirect(reverse('services'))

    form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
