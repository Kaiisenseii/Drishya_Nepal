'''
This models.py contains classes about Customer and Feedback
'''
from django.db import models
from Authentication.models import DrishyaNepalUser

class Customer(models.Model):
    '''
    This class contains customer customer details
    '''
    photographer = models.ForeignKey('service_provider.Photographer', on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.name)
    

class Feedback(models.Model):
    '''
    This class contains feedback system
    '''
    customer = models.ForeignKey(DrishyaNepalUser, on_delete = models.CASCADE)
    photographer = models.ForeignKey('service_provider.Photographer', on_delete=models.CASCADE)
    message = models.CharField(max_length= 200)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    hire = models.ForeignKey("management.Hire",on_delete = models.CASCADE, null=True,)

    def __str__(self):
        return str(self.message)
    
    def get_rating_html(self):
        return "<i class='text-warning mr-1 fa fa-star m-1'></i>" * int(self.rating) + "<i class='text-warning mr-1 m-1 far fa-star'></i>" * (5- int(self.rating))
        
