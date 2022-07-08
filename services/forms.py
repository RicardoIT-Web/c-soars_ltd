from django import forms
from .models import Service, Category


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        desc_names = [(c.id, c.get_description()) for c in categories]

        self.fields['category'].choices = desc_names
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'border-black rounded-1'
