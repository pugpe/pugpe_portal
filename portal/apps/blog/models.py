#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField

class Post(models.Model):
    title = models.CharField(verbose_name=u'Título', max_length=200)
    slug = models.SlugField(verbose_name=u'Slug', max_length=200)
    content = models.TextField(verbose_name=u'Conteúdo')
    pub_date = models.DateTimeField(verbose_name=u'Data de Publicação', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=u'Autor')
    tags = TagField(verbose_name=u'Tags')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Post'
        ordering = ['-pub_date']