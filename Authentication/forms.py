from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class DrishyaNepalUserForm(DrishayNepalUser):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'profile_pic')