# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Speaker(models.Model):

    user            = models.ForeignKey(User, verbose_name=u'Usuario')
    link            = models.CharField(verbose_name=u'Link', max_length=200)
    about_speaker   = models.TextField(verbose_name=u'Descricao')
    pub_date        = models.DateTimeField(default=datetime.now, verbose_name=u'Data de Publicação', auto_now_add=True)


    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        ordering = ('-pub_date',)


class Lecture(models.Model):

    title           = models.CharField(verbose_name=u'Título', max_length=200)
    speaker         = models.ForeignKey(Speaker, verbose_name=u'Palestrante')
    author          = models.ForeignKey(User, verbose_name=u'Autor')
    description     = models.TextField(verbose_name=u'Descricao')
    duration        = models.IntegerField(verbose_name=u'Duração (minutos)')
    pub_date        = models.DateTimeField(default=datetime.now, verbose_name=u'Data de Publicação', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
