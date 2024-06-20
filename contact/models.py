from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField()
    call= models.CharField(max_length=20)
    locations = models.CharField(max_length=50)
    subject = models.CharField(max_length=50) 
    message = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.name)