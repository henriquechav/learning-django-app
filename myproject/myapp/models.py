from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

# class User(models.Model):
#     username = models.CharField(max_length=)
#     password = models.CharField(max_length=)
