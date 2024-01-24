from django.db import models
from django.contrib.auth.models import AbstractUser


class DrishyaNepalUser(AbstractUser):
    """Custom User model for authentication."""
    #: A string representing the full name of this user.
    address = models.CharField(max_length=254)
    profile_pic = models.ImageField(upload_to="users")
    phone = models.CharField(max_length=254)
    
    is_photographer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    
    