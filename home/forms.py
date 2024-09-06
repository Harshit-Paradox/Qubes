# forms.py
from django import forms
from .models import Contact , Affilate , Builder , Details , Career


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class AffilateForm(forms.ModelForm):
    class Meta:
        model = Affilate
        fields = ['name', 'number']


class BuilderForm(forms.ModelForm):
    class Meta:
        model = Builder
        fields = ['user_type', 'name', 'number']

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'email', 'number', 'city', 'position', 'resume']

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'contact_number', 'rera_number', 'location']