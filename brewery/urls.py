# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PlaceList,PlaceDetail

urlpatterns = [
    url(r'^$', PlaceList.as_view(), name='place_list'),
    url(r'^(?P<slug>[\w-]+)/$', PlaceDetail.as_view(), name='place_detail'),
]