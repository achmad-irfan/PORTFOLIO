from django.db import models

# Create your models here.


class Skillsss(models.Model):
    skill_names = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/')

    def _str_(self):
        return "{}".format(self.skill_names)
