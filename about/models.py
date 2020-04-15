from django.db import models


# Create your models here.

class About(models.Model):
    fullName = models.CharField(max_length=100)
    dateOfBirth = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
