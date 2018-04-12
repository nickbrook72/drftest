# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Album(models.Model):
    name = models.CharField(blank=True, null=True, max_length=75, unique=True)


class Track(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=64)
    is_shared = models.BooleanField()
