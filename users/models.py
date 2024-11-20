from django.db import models

# Create your models here.
class Users(models.Model):
    class RoleChoices(models.TextChoices):
        ADMIN = ("AD", "Admin")
        MODERATOR = ("MD", "Moderator")
        SELLER = ("SL", "Seller")
        BUYER = ("BY", "Buyer")

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.TextField()

    role = models.CharField(max_length=2, choices=RoleChoices)