from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title