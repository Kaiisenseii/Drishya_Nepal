'''
This models.py contains classes about Information and Developer
'''
from django.db import models

class Information(models.Model):
    '''
    This class contains information about website
    '''
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    address = models.CharField(max_length = 200)
    phone_number = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.name)


class Developer(models.Model):
    '''
    This class contains developer details
    '''
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.name)
    