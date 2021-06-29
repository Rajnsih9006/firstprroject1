from django.db import models
from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    city = models.CharField(max_length=20)



