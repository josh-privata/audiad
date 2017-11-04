from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.LocationList.as_view(), name='list'),
    url(r'^new/$', views.LocationCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.LocationDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.LocationUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.LocationDelete.as_view(), name='delete'),
]
