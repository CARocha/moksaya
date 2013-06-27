#Views file inside Moksaya 
#ToDO- this is just experimental , doing this to learn how to serve user uploaded files in django templates
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as Signout
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.generic.list import ListView
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect
from projects.models import *
from userena.forms import (SignupForm, SignupFormOnlyEmail, AuthenticationForm,
                           ChangeEmailForm, EditProfileForm)
from userena.models import UserenaSignup
from userena.decorators import secure_required
from userena.backends import UserenaAuthenticationBackend
from userena.utils import signin_redirect, get_profile_model, get_user_model
from userena import signals as userena_signals
from userena import settings as userena_settings

from guardian.decorators import permission_required_or_403

import warnings

from django.shortcuts import render_to_response, RequestContext
from django.views.generic.simple import direct_to_template
from account.models import Account
from profiles.models import *
from projects.models import *
from django.contrib.auth.models import User
from userena import views as userena_views 


def Profiler(request):

    if request.user.is_authenticated():
	    profile = Profile.objects.get(user=request.user)
	    project = Projects.objects.filter(owner=request.user)
	    

	    return render_to_response('profile.html', locals() ,context_instance= RequestContext(request))

    else:
        return render_to_response('profile.html')


def moksaya_profile(request,username):
	
#	if username == request.user:
               
    user = get_object_or_404(get_user_model(),username__iexact=username)
    #project =  Projects.objects.filter(owner=request.user)
    profile_model = get_profile_model()
    project = Projects.objects.filter(owner=request.user)
    try:
        profile = user.get_profile()
    except profile_model.DoesNotExist:
        profile = profile_model.objects.create(user=user)

    if not profile.can_view_profile(request.user):
        return HttpResponseForbidden(_("You don't have permission to view this profile."))
 
    response = userena_views.profile_detail(request, request.user,extra_context={"project":project})

    return response



