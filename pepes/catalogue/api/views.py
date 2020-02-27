from rest_framework import generics
from catalogue import Pepe
from . import serializers


class PepeView(generics.ModelViewSet):
    queryset = Pepe.objects.all()
    serializer_class = serializers.PepeSerializer