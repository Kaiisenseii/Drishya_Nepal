from .models import Hire
from django import forms


class HireForm(forms.ModelForm):
    class Meta:
        model = Hire
        fields = "__all__"



    