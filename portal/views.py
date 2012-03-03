from django.shortcuts import render_to_response
from django.template import RequestContext

from portal.apps.blog.models import Post

def home(request):
    latest_posts = Post.objects.filter()[:6]

    ctx = {'latest_posts': latest_posts }
    return render_to_response('index.html', ctx,
                              RequestContext(request))
