from django import forms 
from .models import Equipment, Photo



class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'



        

