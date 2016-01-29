from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoCMSDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns = patterns('',
#        url(r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
#    ) + urlpatterns

if settings.DEBUG: 
    urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
