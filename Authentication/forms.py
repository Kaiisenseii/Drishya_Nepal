from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ("__all__")



