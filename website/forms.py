
from django import forms
from service_provider.models import Services, Photo
from . models import Contact

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PhotographerPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        
