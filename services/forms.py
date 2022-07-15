from django import forms
from .models import Service, Category


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = ('status', 'grand_total',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-1'
