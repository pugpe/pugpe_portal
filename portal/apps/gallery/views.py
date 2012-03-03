from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Album, Photo


def list_albuns(request):
    albuns = Album.objects.all()

    ctx = {'albuns': albuns}
    return render_to_response('gallery/albuns.html', ctx,
                              RequestContext(request))

def view_album(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)
    photos = Photo.objects.filter(album=album.id)

    ctx = {'album': album, 'photos': photos}
    return render_to_response('gallery/album.html', ctx,
                              RequestContext(request))
