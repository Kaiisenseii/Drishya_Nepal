from django.db import models

class Website(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    address = models.CharField(max_length = 200)
    phone_number = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.name)


class Developer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.name)
    