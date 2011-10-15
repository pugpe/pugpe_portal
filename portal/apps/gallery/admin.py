from django.contrib import admin
from models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'created')


admin.site.register(Photo, PhotoAdmin)
