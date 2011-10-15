#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField()

    def __unicode__(self):
      return self.title