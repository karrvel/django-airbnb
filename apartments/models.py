from django.db import models

class Apartment(models.Model):
    class StatusChoices(models.TextChoices):
        REVIEW = ('r', 'REVIEW')
        REJECT = ('x', 'REJECT')
        ACCEPT = ('a', 'ACCEPT')


    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.CharField(max_length=200)
    daily_price = models.FloatField()
    owner = models.ForeignKey('users.Users', on_delete=models.RESTRICT)
    desciprtion = models.TextField()
    likes = models.IntegerField(default=0)
    image = models.ImageField()
    status = models.CharField(max_length=1, choices=StatusChoices, default=StatusChoices.REVIEW)