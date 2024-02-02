from .models import Feedback
from django import forms

class FeedBackForm(forms.ModelForm):
    class Meta:
        model  = Feedback
        fields = "__all__"