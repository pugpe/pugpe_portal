#!/usr/bin/python
#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from portal.settings import MEDIA_ROOT
import os

class Badge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/badges')
    owners = models.ManyToManyField(User, verbose_name="list of owners")

    def __unicode__(self):
        return self.name
