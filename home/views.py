from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import ReviewCard


def index(request):
    """ View to render index page"""

    return render(request, 'home/index.html')


def user_review(request, service_name):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews = ReviewCard.objects.get(user__id=request.user.id, service_name=service_name)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, "Thank you for your review.")
            return redirect(url)
        except ReviewCard.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewCard()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.service_name = service_name
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thank you for your review.")
                return redirect(url)
