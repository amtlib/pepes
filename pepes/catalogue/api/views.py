from catalogue.models import Pepe
from rest_framework import viewsets
from . import serializers


class PepeView(viewsets.ModelViewSet):
    queryset = Pepe.objects.all()
    serializer_class = serializers.PepeSerializer