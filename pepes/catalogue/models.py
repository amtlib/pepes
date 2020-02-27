from django.db import models


class Pepe(models.Model):
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField()
    