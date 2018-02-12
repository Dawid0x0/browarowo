# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Place

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
    