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
    
    
class Chat(models.Model):
    """A chat between two or more users."""
    to_user = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="from_user")
    
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return "From " + str(self.from_user.get_full_name()) + "To " + str(self.to_user.get_full_name())

class Notification(models.Model):
    '''This is a class where when hired notification is sent to respective user'''
    message = models.CharField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default = False)
    user = models.ForeignKey(DrishyaNepalUser,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.message)

class Otp(models.Model):
    '''This is used to send OTPs'''
    user = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    otp = models.IntegerField()
    
     
    def __str__(self):
        return str(self.user.email) + " - "+ str(self.otp)