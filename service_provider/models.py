'''
This models.py contains classes like Photographer, Photo, Equipment, Services
'''
from django.db import models
from Authentication.models import DrishyaNepalUser
from client.models import Feedback

class Tag(models.Model):
    name = models.CharField(max_length=254) 
    
    def __str__(self):
        return str(self.name)
    
    
class Photographer(models.Model):
    '''
    This class is for photographer details
    '''
    STATUS_CHOICES = (
        ('Available', 'Available'), 
        ('Booked', 'Booked'), 
        ("Not Available", 'Not Available'), 
        ('Busy', 'Busy')
    )
    user = models.OneToOneField(DrishyaNepalUser, on_delete=models.CASCADE, related_name="photographer")
    experience = models.CharField(max_length = 254)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=254, choices=STATUS_CHOICES)
    is_available = models.BooleanField(default = True)
    is_videographer = models.BooleanField(default=False)
 
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.user.get_full_name())
    
    def get_avg_rating_html(self):
        ratings = Feedback.objects.all().filter(photographer=self)
        summation = 0
        for rate in ratings:
            summation += rate.rating
        average = summation / ratings.count() if ratings.count() > 0 else 0
        return "<i class='text-warning mr-2 fa fa-star  '></i>" * int(average) + "<i class='text-warning mr-1  far fa-star '></i>" * (5- int(average))
    
    
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
    