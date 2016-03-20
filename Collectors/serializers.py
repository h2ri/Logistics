from rest_framework import serializers
from . import models
from .models import Clients,Collectors,PostalCode

class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostalCode

class CollectersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collectors

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients

