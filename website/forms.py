
from django import forms
from service_provider.models import Services
from . models import Contact

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        