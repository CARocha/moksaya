#Views file inside Moksaya 
#ToDO- this is just experimental , doing this to learn how to serve user uploaded files in django templates

from django.shortcuts import render_to_response, RequestContext
from account.models import Account
from django.contrib.auth.models import User


def Profiler(request):

    profile = Account.objects.get(user=request.user)

    return render_to_response('profile.html', locals() ,context_instance= RequestContext(request))

