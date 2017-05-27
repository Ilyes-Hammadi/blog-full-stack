from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from users.models import Profile

# Create your models here.
class Article(models.Model):
    profile = models.ForeignKey(Profile, default=1)

    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title