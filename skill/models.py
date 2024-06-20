from django.db import models

# Create your models here.


class skill(models.Model):
    skill_name = models.CharField(max_length=50)
    image = models.ImageField()

    def _str_(self):
        return "{}".format(self.name)
