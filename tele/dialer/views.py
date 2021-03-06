from django.contrib.auth.decorators import login_required

from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.conf import settings 
from django.views.decorators.csrf import csrf_exempt

from twilio.rest import TwilioRestClient
from twilio.util import TwilioCapability
# Create your views here.
from dialer.models import CallForm


def index(request):
    return render(request, 'dialer/index.html', {})

@login_required(login_url='/dialer/accounts/login')
def call(request): 
    if request.method == "POST": 
        us_call = CallForm(request.POST) 
        return HttpResponseRedirect('/dialer/call')
    else: 
        c = {}
        c.update(csrf(request)) 
        c.update({"token": generate_token()})
        c.update({"Call": CallForm()})
        return render_to_response('dialer/call.html', c)

@csrf_exempt
def incoming(request): 
    q = request.GET
    phone_number = q['PhoneNumber'] 
    c = {"To": "+"+phone_number}
    return render_to_response('dialer/incoming.xml', c)

def generate_token():
    ACCOUNT_SID = settings.ACCOUNT_SID
    AUTH_TOKEN = settings.AUTH_TOKEN

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    apps = client.applications.list()
    application = apps[0]
    sid = application.sid

    capability = TwilioCapability(ACCOUNT_SID, AUTH_TOKEN)
    capability.allow_client_outgoing(sid)
    return capability.generate()
