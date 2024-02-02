'''
This models.py contains Hiring class for photographer
'''
from django.db import models
from service_provider.models import  Services
from Authentication.models import DrishyaNepalUser
class Hire(models.Model):
    '''
    This class is the function to hire the photographer by customer
    '''
    photographer = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="provider")
    customer = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="customer")
    location = models.CharField(max_length = 200)
    date = models.DateField()
    #PRICE KO LAGI SERVICE NAME NAI LEKHEKO
    service = models.ForeignKey(Services, on_delete  = models.CASCADE)
    description = models.CharField(max_length = 200)
    
    def __str__(self):
        return str(self.location)
    
class Testimonial(models.Model):
    '''
    Model representing testimonials of advertisement in drishyanepal
    '''
    logo = models.ImageField(upload_to='testimonial/')
    description = models.CharField(max_length = 254)
    name = models.CharField(max_length=254)