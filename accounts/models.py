from django.db import models


class Account(models.Model):

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    adress = models.CharField(max_length=1000)
    avatar = models.ImageField(upload_to=None)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
