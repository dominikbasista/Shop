from django.db import models


class Account(models.Model):

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    adress = models.CharField(max_length=1000, null=True)
    avatar = models.ImageField(upload_to=None, null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
