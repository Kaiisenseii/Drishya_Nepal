'''
This models.py contains classes like Photographer, Photo, Equipment, Services
'''
from django.db import models
from Authentication.models import DrishyaNepalUser

class Tag(models.Model):
    name = models.CharField(max_length=254) 
    
    def __str__(self):
        return str(self.name)
class Photographer(models.Model):
    '''
    This class is for photographer details
    '''
    user = models.OneToOneField(DrishyaNepalUser, on_delete=models.CASCADE)
    experience = models.CharField(max_length = 254)
    tags = models.ManyToManyField(Tag)
    is_available = models.BooleanField(default = True)
    is_videographer = models.BooleanField(default=False)
 
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.user)
     
class Photo(models.Model):
    '''
    This class is for the photos uploaded by photographers
    '''
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 254)
    description = models.CharField(max_length = 254)
    type = models.CharField(max_length = 254)
    date_taken = models.DateField(null=True, blank=True)
    photo = models.ImageField()
    
    def __str__(self):
        return str(self.name)

class Equipment(models.Model):
    '''
    This class is for the which type of equipment does photographer have
    '''
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 254)
    photo = models.ImageField(upload_to = 'equipment/')
    
    def __str__(self):
        return str(self.name)
    
class Services(models.Model):
    '''
    This class is for what type of services photographer can give
    '''
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 254)
    price = models.PositiveIntegerField()
    duration = models.CharField(max_length = 254)
    
    def __str__(self):
        return f"{self.name} - Rs. {self.price} - {self.duration} days"
    