# -*- coding:utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save

class Album(models.Model):
    user = models.ForeignKey(User, related_name='user_album')
    cover = models.ImageField(upload_to='uploads/gallery')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

class Photo(models.Model):
    album = models.ForeignKey(Album)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/gallery')
    created = models.DateTimeField(auto_now_add=True)


#função para criar o campo slug do album
def create_album_slug(signal, sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

#chama signal pre_save e passa a função create_album_slug
pre_save.connect(create_album_slug, sender=Album)
    

