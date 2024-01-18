'''
This models.py contains Hiring class for photographer
'''
from django.db import models
from service_provider.models import Photographer
from client.models import Customer

class Hire(models.Model):
    '''
    This class is the function to hire the photographer by customer
    '''
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.CharField(max_length = 200)
    date = models.DateField()
    price = models.PositiveIntegerField()
    description = models.CharField(max_length = 200)
    
    def __str__(self):
        return str(self.location)
