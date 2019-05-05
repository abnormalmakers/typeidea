from django.db import models

# Create your models here.
class ManyA(models.Model):
    name=models.CharField(max_length=10)




class ManyB(models.Model):
    name=models.CharField(max_length=10)
    manya = models.ManyToManyField(ManyA)