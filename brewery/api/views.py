# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from brewery.models import Place
from .serializers import PlaceSerializer, PlaceMapViewAddressSerializer

class PlaceListAPIView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}
    
class PlaceRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
class PlaceAPICreate(CreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
class PlaceAPIUpdate(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
class PlaceAPIDelete(RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
class PlaceMapsAddressView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = PlaceMapViewAddressSerializer
    queryset = Place.objects.all()