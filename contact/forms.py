from django import forms
from .models import ContactModel
from django.core.validators import RegexValidator


class ContactForm(forms.ModelForm):
    phoneRegex = RegexValidator(
        regex=r'\+\d{1,3}-\d{1,15}',
        message='Phone not valid'
    )

    class Meta:
        model = ContactModel
        fields = '__all__'

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
