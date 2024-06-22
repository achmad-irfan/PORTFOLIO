from django.db import models

# Create your models here.


class listskill(models.Model):
    name_skill = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name_skill
