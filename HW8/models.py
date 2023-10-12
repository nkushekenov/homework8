from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
