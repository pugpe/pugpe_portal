from django.db import models


#class Album(object):
class Photo(models.Model):
    description = models.CharField(max_length=200, 
null=True, blank=True)
    image = models.ImageField(upload_to='uploads/gallery')
    created = models.DateTimeField(auto_now_add=True)
    
    

