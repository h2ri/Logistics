from django.shortcuts import render
from rest_framework import viewsets
from models import PostalCode
from serializers import PostalCodeSerializer,ClientSerializer,CollectersSerializer

# Create your views here.
class PostalCodeViewSet(viewsets.ModelViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer


