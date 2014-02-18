from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.
from dialer.models import CallForm


def index(request):
    return render(request, 'dialer/index.html', {})

def call(request): 
    if request.method == "POST": 
        us_call = CallForm(request.POST) 
        return HttpResponseRedirect('/dialer/call')
    else:
        c = {}
        c.update(csrf(request)) 
        c.update({"Call": CallForm()})
        return render_to_response('dialer/call.html', c)

def incoming(request):
    c = {"To": "+15109084612"}
    return render_to_response('dialer/incoming.xml', c)
