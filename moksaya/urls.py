from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from profiles.forms import SignupFormExtra

from django.contrib import admin
admin.autodiscover()

from profiles.api import ProfileResource , ProjectResource 

from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())
v1_api.register(ProfileResource())
#v1_api.register(UserResource())

#profile_resource = ProfileResource()
#project_resource = ProjectResource()





urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Demo Override the signup form with our own, which includes a
    # first and last name.
    # (r'^accounts/signup/$',
    #  'userena.views.signup',
    #  {'signup_form': SignupFormExtra}),

    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^api/', include(v1_api.urls)),
    #url(r'^api/', include(project_resource.urls)),
                       
    
    (r'^i18n/', include('django.conf.urls.i18n')),
)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


