from django.db import models

# Create your models here.


class Weather(models.Model):
    city = models.CharField(max_length=32)
    temperature = models.CharField(max_length=24)
    description = models.TextField()
    icon = models.CharField(max_length=16)
    updated_date = models.DateTimeField()
    api_response = models.TextField()

    def __str__(self) -> str:
        return self.city
