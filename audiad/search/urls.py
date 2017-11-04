from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SearchList.as_view(), name='list'),
    url(r'^new/$', views.SearchCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.SearchDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.SearchUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.SearchDelete.as_view(), name='delete'),
]
