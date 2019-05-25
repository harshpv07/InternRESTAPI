from rest_framework import serializers
from .models import Songs

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id','url','title','artist')