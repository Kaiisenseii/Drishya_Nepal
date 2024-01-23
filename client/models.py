'''
This models.py contains classes about Customer and Feedback
'''
from django.db import models
from service_provider.models import Photographer

class Customer(models.Model):
    '''
    This class contains customer customer details
    '''
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
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
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    message = models.CharField(max_length = 200)
    rating = models.FloatField()
    
    def __str__(self):
        return str(self.message)
