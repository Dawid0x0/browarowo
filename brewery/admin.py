# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    ordering = ('-timestamps','name')
    empty_value_display = 'unknown'
    fieldsets = (
        (None,{
            'fields':('name','description')
        }),
        ('Adress',{
            'fields':('city','street','number','www')
        }),
        ('Adwanced',{
            'classes': ('collapse',),
            'fields':('slug',)
        }),
    )
    
    list_display = ('name','city','www')
    list_filter = ('city','timestamps')
    readonly_fields = ('slug',)
    search_fields = ('name',)