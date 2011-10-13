from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Album


def list_albuns(request):
    albuns = Album.objects.all()

    ctx = {'albuns': albuns}
    return render_to_response('gallery/albuns.html', ctx,
                              RequestContext(request))
