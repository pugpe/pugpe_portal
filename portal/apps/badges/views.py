#!/usr/bin/python
#-*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Badge

def list_badges(request):
    badges = Badge.objects.all()

    ctx = {'badges': badges}

    return render_to_response('badges/badges.html', ctx,
                              RequestContext(request))
