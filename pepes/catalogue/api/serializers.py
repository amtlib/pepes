from rest_framework import serializers
from catalogue.models import Pepe


class PepeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pepe
        fields = ['pk', 'description', 'image']