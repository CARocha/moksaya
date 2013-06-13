from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView
from moksaya.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^profile/", "moksaya.views.Profiler", name="profile"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

