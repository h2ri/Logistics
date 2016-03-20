from django.shortcuts import render
from rest_framework import viewsets
from models import PostalCode,Collectors,CollectorPinCodeRelation,Clients
from serializers import PostalCodeSerializer,ClientSerializer,CollectersSerializer

# Create your views here.
class PostalCodeViewSet(viewsets.ModelViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer

class CollectorsViewSet(viewsets.ModelViewSet):
    queryset = Collectors.objects.all()
    serializer_class = CollectersSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
