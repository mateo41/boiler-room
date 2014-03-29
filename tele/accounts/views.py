from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

def handle_login(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/dialer/call') 
            else:
                pass
                # Return a 'disabled account' error message
        else:
            pass
            # Return an 'invalid login' error message.
    else:
         c = {}
         c.update(csrf(request))
         return render_to_response("login.html", c) 


