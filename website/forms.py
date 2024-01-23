
from django import forms
from service_provider.models import Services

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        