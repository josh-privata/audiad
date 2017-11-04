from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ImporterList.as_view(), name='list'),
    url(r'^new/$', views.ImporterCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ImporterDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ImporterUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ImporterDelete.as_view(), name='delete'),
]
