# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PlaceList,PlaceDetail,PlaceRUDView,PlaceListAPIView

urlpatterns = [
    url(r'^$', PlaceList.as_view(), name='place-list'),
    url(r'^api/place/$', PlaceListAPIView.as_view(), name='place-api-list'),
    url(r'^api/place/(?P<pk>\d+)/$', PlaceRUDView.as_view(), name='place-api-rud'),
    url(r'^(?P<slug>[\w-]+)/$', PlaceDetail.as_view(), name='place-detail'),
]