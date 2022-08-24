""" Contact Us Views """
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


def index(request):
    """home page view"""
    return render(request, "home/index.html")


def contact(request):
    """a view to render contact form"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = {"subject": form.cleaned_data["subject"]}
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "contact_number": form.cleaned_data["contact_number"],
                "subject": form.cleaned_data["subject"],
                "comment": form.cleaned_data["comment"],
            }
            message = "\n".join(body.values())
            messages.success(request,
                             "Thank you! Your Inquiry has been submitted.\
                              We'll revert back with a response as soon as\
                              possible.",)
            try:
                send_mail(subject, message, "admin@admin.com",
                          ["admin@admin.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header.")
            return redirect(reverse('home'))

    if request.method == 'GET':
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


class Inquiries(ListView):
    """A view to render inquiries"""

    model = Contact
    template_name = "contact/inquiries.html"


@login_required
def edit_inquiries(request, inquiries_id):
    """for administrator to amend status of an inquiry once actioned"""
    inquiries = get_object_or_404(Contact, pk=inquiries_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=inquiries)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inquiry updated successfully!')
            return redirect(reverse('inquiries'))
        else:
            messages.error(request, 'Update Failed.\
                Please ensure the form is valid.')
    else:
        form = ContactForm(instance=inquiries)
        messages.info(request, 'You are about to edit an inquiry form')

    template = 'contact/edit_inquiries.html'
    context = {
        'form': form,
        'inquiries': inquiries,
    }

    return render(request, template, context)


@login_required
def delete_inquiries(request, inquiries_id):
    """delete an inquiry"""
    inquiries = get_object_or_404(Contact, pk=inquiries_id)
    inquiries.delete()
    messages.success(request, 'Inquiry has been deleted')
    return redirect(reverse('inquiries'))
