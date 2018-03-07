# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from .models import Place
from .serializers import PlaceSerializer, PlaceMapViewAddressSerializer

class PlaceList(ListView):
    model = Place
    template_name = 'brewery/place_list.html'
    paginate_by = 4
    
    def get_queryset(self):
        places = Place.objects.all()
        
        #page = self.request.GET.get('page')
        search = self.request.GET.get('search')
        
        if search is not None:
            places = places.filter(Q(name__icontains=search))
        return places
        
class PlaceDetail(DetailView):
    model = Place

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