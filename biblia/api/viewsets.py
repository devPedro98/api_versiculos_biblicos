from biblia import models
from biblia.api import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BibliaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.BibliaSerializer
    queryset = models.Biblia.objects.all()
