from django.db import models

# Create your models here.


class skills(models.Model):
    skill_name = models.CharField(max_length=50)
    ability = models.CharField(max_length=50)

    def _str_(self):
        return "{}".format(self.name)
