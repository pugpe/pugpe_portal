from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import FormPostAlbum

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





@login_required
def post_album(request, form_klass=FormPostAlbum, template="gallery/post_album.html"):
    form = FormPostAlbum(request.POST or None, request.FILES or None,)
    if form.is_valid():
        album = form.save(commit=False)
        album.user = request.user
        album.save()
        return redirect('albuns')
    return render(request, template, {'form': form})

@login_required
def my_albuns(request, template="gallery/my_albuns.html"):
    albuns = Album.objects.filter(user=request.user).order_by('-created')
    ctx = {'albuns': albuns}
    return render(request, template, ctx)

@login_required
def edit(request, slug,tempalte="gallery/edit.html", form_klass=FormPostAlbum):
    album_instance = get_object_or_404(Album, slug__iexact=slug)
    form = form_klass(request.POST or None, request.FILES or None, instance=album_instance)
    if form.is_valid():
        album = form.save(commit=False)
        album.user = request.user
        album.save()
        return redirect('act_my_albuns')
    return render(request, tempalte, {'form':form})

