from django.db import models
import csv
# Create your models here.


class EchrDetail(models.Model):
    country = models.CharField(max_length=100)
    ratDate = models.DateField()

    def __str__(self):
        return self.country
