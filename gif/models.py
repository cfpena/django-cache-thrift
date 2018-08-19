from django.db import models

class Gif(models.Model):
    url = models.URLField()
    description = models.TextField()
    views = models.IntegerField(default=0)
