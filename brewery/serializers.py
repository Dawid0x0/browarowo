from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Place
        fields = ['pk','name','description','city','street','number','www','slug','timestamps','url']
        read_only_fields = ['pk','slug','timestamps','url']
        
    def get_url(self,obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)