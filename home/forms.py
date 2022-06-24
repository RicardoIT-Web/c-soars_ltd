from django import forms
from .models import ReviewCard


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewCard
        fields = ['service', 'comment', 'rating']
