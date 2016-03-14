from django.db import models


class Panda(models.Model):
    name = models.CharField(max_length=1000)
    weight = models.IntegerField()
