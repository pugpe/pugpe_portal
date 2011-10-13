from django.contrib import admin
from models import Photo, Album


class PhotoInline(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('description', 'created')
    prepopulated_fields = {'slug': ('description',)}
    inlines = (PhotoInline,)


admin.site.register(Album, AlbumAdmin)
