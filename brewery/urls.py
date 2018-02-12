# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PlaceList,PlaceDetail,PlaceRudView

urlpatterns = [
    url(r'^$', PlaceList.as_view(), name='place_list'),
    url(r'^api/rest/(?P<pk>\d+)/$', PlaceRudView.as_view(), name='place_post_rud'),
    url(r'^(?P<slug>[\w-]+)/$', PlaceDetail.as_view(), name='place_detail'),
]