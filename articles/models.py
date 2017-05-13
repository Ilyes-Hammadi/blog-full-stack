from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title