from django.db import models
# Create your models here.


class CourtDetail(models.Model):
    country = models.CharField(max_length=100)
    proceedingType1 = models.CharField(max_length=200)
    court1 = models.CharField(max_length=300)
    proceedingType2 = models.CharField(max_length=200)
    court2 = models.CharField(max_length=300)
    proceedingType3 = models.CharField(max_length=200)
    court3 = models.CharField(max_length=300)

    def __str__(self):
        return self.country
