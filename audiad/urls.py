from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^album/', include('audiad.album.urls', namespace='album')),
    url(r'^artist/', include('audiad.artist.urls', namespace='artist')),
    url(r'^song/', include('audiad.song.urls', namespace='song')),
    url(r'^common/', include('audiad.common.urls', namespace='common')),
    url(r'^importer/', include('audiad.importer.urls', namespace='importer')),
    url(r'^search/', include('audiad.search.urls', namespace='search')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
