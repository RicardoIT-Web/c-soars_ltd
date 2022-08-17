""" Contact Us Views """
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
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
            if request.user.is_authenticated:
                form.instance.user = request.user
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
            messages.success(
                request,
                "Thank you! Your Inquiry has been submitted.\
                            We'll revert back with a response as soon as\
                            possible",
            )
            try:
                send_mail(subject, message, "admin@admin.com",
                          ["admin@admin.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header.")

    if request.method == 'GET':
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


class Inquiries(ListView):
    """View to render all inquiries"""

    model = Contact
    template_name = "contact/inquiries.html"
