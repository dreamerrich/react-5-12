from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    