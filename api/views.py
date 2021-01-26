from django.shortcuts import render

from rest_framework import viewsets
from .serializers import EcomSerializer
from .models import Ecom

# Create your views here.

class EcomViewSet(viewsets.ModelViewSet):
    queryset=Ecom.objects.all().order_by("title")
    serializer_class=EcomSerializer
