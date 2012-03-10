# -*- coding:utf-8 -*-
from django import forms

from apps.gallery.models import Album


class FormPostAlbum(forms.ModelForm):
    class Meta:
        model = Album
