from rest_framework import serializers
from . import models

class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostalCode

class CollectersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collectors

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Clients
