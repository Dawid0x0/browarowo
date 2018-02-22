# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Place

class PlaceAdmin(admin.ModelAdmin):
    pass
    #prepopulated_fields = {'slug': ('name',)}

admin.site.register(Place,PlaceAdmin)
