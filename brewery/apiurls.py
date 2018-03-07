# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PlaceList,PlaceDetail,PlaceRUDView,PlaceListAPIView,PlaceAPICreate,PlaceAPIUpdate,PlaceAPIDelete,PlaceMapsAddressView

urlpatterns = [
    url(r'^$', PlaceListAPIView.as_view(), name='place-api-list'),
    url(r'^create$', PlaceAPICreate.as_view(), name='place-api-create'),
    url(r'^(?P<pk>\d+)/update/$', PlaceAPIUpdate.as_view(), name='place-api-update'),
    url(r'^(?P<pk>\d+)/delete/$', PlaceAPIDelete.as_view(), name='place-api-delete'),
    url(r'^(?P<pk>\d+)/$', PlaceRUDView.as_view(), name='place-api-rud'),
    url(r'^(?P<slug>[\w-]+)/$', PlaceMapsAddressView.as_view(), name='place-maps-view-address'),
]