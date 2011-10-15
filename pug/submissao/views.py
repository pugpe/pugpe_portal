from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Palestrante
from forms import Test, PalestranteForm

def hello(request):
    #import pdb; pdb.set_trace()
    form = Test()

    if request.method == 'POST':
        p_form = PalestranteForm(request.POST)
        if p_form.is_valid():
            # fazer alguma coisa daqui a pouco
            p_form.save()
    else:
        p_form = PalestranteForm()


    palestrantes = Palestrante.objects.all()

    return render_to_response('submissao/hello.html', {'palestrantes': palestrantes, 'form': form, 
   'p_form': p_form}, RequestContext(request))

