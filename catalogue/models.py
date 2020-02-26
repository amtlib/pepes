from django.db import models
from datetime import datetime


class Pepe(models.model):
    description = models.TextField(max_length=200)
    image = models.ImageField()
    uploaded_at = models.DateTimeField(default=datetime.now)
    