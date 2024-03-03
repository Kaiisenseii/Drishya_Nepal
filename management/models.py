'''
This models.py contains Hiring class for photographer
'''
from django.db import models
from service_provider.models import  Services
from Authentication.models import DrishyaNepalUser
from client.models import Feedback



class Hire(models.Model):
    '''
    This class is the function to hire the photographer by customer
    '''
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Hired", "Hired"),
        ('Not Hired', 'Not Hired'),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
    )
    
    photographer = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="provider")
    customer = models.ForeignKey(DrishyaNepalUser, on_delete=models.CASCADE, related_name="customer")
    location = models.CharField(max_length = 200)
    date = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Pending")
    #PRICE KO LAGI SERVICE NAME NAI LEKHEKO
    service = models.ForeignKey(Services, on_delete  = models.CASCADE)
    description = models.CharField(max_length = 200)
    
    def has_feedback(self):
        feedback = Feedback.objects.all().filter(customer=self.customer, photographer=self.photographer.photographer, hire=self)
        if feedback.exists():
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.location)
    
class Testimonial(models.Model):
    '''
    Model representing testimonials of advertisement in drishyanepal
    '''
    logo = models.ImageField(upload_to='testimonial/')
    description = models.CharField(max_length = 254)
    name = models.CharField(max_length=254)