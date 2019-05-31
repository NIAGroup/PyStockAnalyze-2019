from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    #imgSrc = models.TextField()
    urlSrc = models.TextField()
    description = models.TextField()
    summary = models.TextField()