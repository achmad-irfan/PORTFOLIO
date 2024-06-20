from django.db import models

# Create your models here.


class skillsss(models.Model):
    skill_names = models.CharField(max_length=50)
    image = models.ImageField()

    def _str_(self):
        return "{}".format(self.name)
