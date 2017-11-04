from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.AlbumList.as_view(), name='list'),
    url(r'^new/$', views.AlbumCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.AlbumDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.AlbumUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='delete'),
]
