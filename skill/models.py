from django.db import models

# Create your models here.


class ListSkill(models.Model):
    name_skill = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/')

    def _str_(self):
        return "{}".format(self.name_skill)
