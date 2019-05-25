from django.shortcuts import render
from rest_framework import viewsets
from .models import Songs
from .serializers import SongSerializers

class SongView(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializers 
# Create your views here.
