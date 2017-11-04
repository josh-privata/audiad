from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SongList.as_view(), name='list'),
    url(r'^new/$', views.SongCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.SongDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.SongUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.SongDelete.as_view(), name='delete'),
]
