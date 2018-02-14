# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.
class PlaceList(ListView):
    model = Place
    template_name = 'brewery/place_list.html'
    
    def get_queryset(self):
        places = Place.objects.all()
        paginator = Paginator(places, 4)
        page = self.request.GET.get('page')
        
        try:
            place = paginator.page(page)
        except PageNotAnInteger:
            place = paginator.page(1)
        except EmptyPage:
            place = paginator.page(paginator.num_pages)
        return place
            
class PlaceDetail(DetailView):
    model = Place

class PlaceListAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}
    
class PlaceRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()