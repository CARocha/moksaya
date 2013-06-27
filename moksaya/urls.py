from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView
from moksaya.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()
from userena import views as userena_views
from userena import settings as userena_settings



urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^profile/", "moksaya.views.Profiler", name="profile"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^friends/", include("friendship.urls")),
    url(r"^project/", TemplateView.as_view(template_name="project.html"), name="project"),
    url(r'^accounts/(?P<username>(?!signout|signup|signin)[\.\w-]+)/$',"moksaya.views.moksaya_profile", name='userena_profile_detail'),                   
    url(r'^userena/', include('userena.urls')),
    #url(r"^profiles/", include("idios.urls")),                   
)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

