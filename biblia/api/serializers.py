from biblia import models
from rest_framework import serializers


class BibliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biblia
        fields = '__all__'
