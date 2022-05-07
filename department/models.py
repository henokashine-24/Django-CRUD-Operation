from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    depart = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    hired = models.IntegerField()


    def __str__(self):
        return self.name
