# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Place

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
