from django.db import models

class Information(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    address = models.CharField(max_length = 200)
    phone_number = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.name)


class Developer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.name)

class About(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to= "about/")
    
    def __str__(self):
        return str(self.name)    
    
class Contact(models.Model):
    name = models.CharField(max_length=254)
    subject = models.CharField(max_length=256, default="No Subject ")
    email = models.EmailField()
    message = models.CharField(max_length = 254)
    
    def __str__(self):
        return str(self.name)
    