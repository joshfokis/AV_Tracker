from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'api/^$', views.api_root),
    url(r'^api/av/$', views.av_list.as_view(), name='av-list'),
    url(r'^api/av/(?P<pk>[0-9]+)/$', views.av_detail.as_view(), name='av_detail'),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-details'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]