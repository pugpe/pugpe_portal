from django.db import models


class Album(models.Model):
    cover = models.ImageField(upload_to='uploads/gallery')
    description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

class Photo(models.Model):
    album = models.ForeignKey(Album)
    description = models.CharField(max_length=200, 
null=True, blank=True)
    image = models.ImageField(upload_to='uploads/gallery')
    created = models.DateTimeField(auto_now_add=True)
