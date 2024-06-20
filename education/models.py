from django.db import models
from datetime import date


# Create your models here.
class school(models.Model):
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=25)
    college = models.CharField(max_length=50)
    finish = models.DateField(default='2000-03-03')

    def __str__(self):
        return "{}".format(self.college)


class certification(models.Model):
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=15)
    certifier = models.CharField(max_length=50)
    finish = models.DateField(default='2000-03-03')

    def __str__(self):
        return "{}".format(self.major)


class projectExp(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    background = models.CharField(max_length=500)
    finish = models.DateField()
    jobdesk1 = models.TextField(blank=True)
    jobdesk2 = models.TextField(blank=True)
    jobdesk3 = models.TextField(blank=True)
    jobdesk4 = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.title)


class workExp(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    year = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    finish = models.DateField()
    jobdesk1 = models.TextField(blank=True)
    jobdesk2 = models.TextField(blank=True)
    jobdesk3 = models.TextField(blank=True)
    jobdesk4 = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.title)
