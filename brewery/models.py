# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework.reverse import reverse
from .tool import random_slug

class Place(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True,null=True) 
    city = models.CharField(max_length=200,blank=True,null=True)
    street = models.CharField(max_length=200,blank=True,null=True)
    number = models.CharField(max_length=10,blank=True,null=True)
    www = models.URLField(blank=True,null=True)
    slug = models.SlugField(max_length=300)
    timestamps = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
        
    def get_api_url(self,request=None):
        return reverse('place-api-rud', kwargs={'pk':self.pk},request=request)

@receiver(pre_save, sender=Place)
def my_handler(sender, instance, *args, **kwargs):
	slug = slugify(instance.name)
	slug_exists = Place.objects.filter(slug=slug).exists()
	if slug_exists:
		instance.slug = random_slug(slug)
	else:
		instance.slug = slug