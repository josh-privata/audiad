from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ArtistList.as_view(), name='list'),
    url(r'^new/$', views.ArtistCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ArtistDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ArtistUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ArtistDelete.as_view(), name='delete'),
]
