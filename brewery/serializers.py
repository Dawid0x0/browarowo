from rest_framework import serializers
from .models import Place

class PlacePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['pk','name','description','city','street','number','www','slug','timestamps']