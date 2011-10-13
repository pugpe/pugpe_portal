#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post

def posts(request, template='blog/posts.html'):
    return object_list(request,
                       Post.objects.all(),
                       template_name=template,
                       paginate_by=5
    )

def post(request, slug, template='blog/post.html'):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response(template, {'post':post}, RequestContext(request))