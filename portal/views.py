from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('index.html',context_instance = RequestContext(request))

def guideline(request):
    return render_to_response('guideline.html',context_instance = RequestContext(request))
