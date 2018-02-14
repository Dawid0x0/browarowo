# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from rest_framework.reverse import reverse

class Place(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True,null=True) 
    city = models.CharField(max_length=200,blank=True,null=True)
    street = models.CharField(max_length=200,blank=True,null=True)
    number = models.CharField(max_length=10,blank=True,null=True)
    www = models.URLField(blank=True,null=True)
    slug = models.SlugField(max_length=300,unique=True)
    timestamps = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
        
    def get_api_url(self,request=None):
        return reverse('place-api-rud', kwargs={'pk':self.pk},request=request)