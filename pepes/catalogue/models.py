from django.db import models


class Pepe(models.Model):
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
    return self.description[:20]