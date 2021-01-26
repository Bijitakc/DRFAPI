from rest_framework import serializers
from .models import Ecom

class EcomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Ecom
        fields=('image','title','price')