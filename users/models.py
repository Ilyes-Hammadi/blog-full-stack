# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')

    def __str__(self):
        return 'id: {0}, username: {1}'.format(self.id, self.user.username)
