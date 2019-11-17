from django.db import models
# Create your models here.


class CourtDetail(models.Model):
    country = models.CharField(max_length=100)
    proceedingType = models.CharField(max_length=200)
    court = models.CharField(max_length=300)

    def __str__(self):
        return self.country
