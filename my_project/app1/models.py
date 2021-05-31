from django.db import models



# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=35)
    emailid=models.EmailField(max_length=29)
    mobile=models.CharField(max_length=30)
    dat=models.DateTimeField()

    def __str__(self):
        return self.name