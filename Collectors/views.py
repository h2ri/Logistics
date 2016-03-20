from django.shortcuts import render
from rest_framework import viewsets
from models import PostalCode,Collectors,CollectorPinCodeRelation,Clients
from serializers import PostalCodeSerializer,ClientSerializer,CollectersSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
import itertools,requests,re,scipy
from . import tsp

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

class route(APIView):
    def get(self,request,*args,**kwargs):
        collecter = Collectors.objects.get(id = 1)
        c = Clients.objects.filter(postalCode = PostalCode.objects.get(postalCode=560038))

        matrix = [[0 for x in range(len(c)+1)] for x in range(len(c))]
        print matrix
        count = 0
        for x in c:
            matrix[count][0] = x.name
            for i in range(len(c)):
                if matrix[count][i+1] == 0:
                    print c[i]
                    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+str(x.addressLatitude)+','+str(x.addressLogitude)+'&destination='+str(c[i].addressLatitude)+','+str(c[i].addressLogitude)+'&key=AIzaSyCOKScAM0z68czlcG7wxzbeQAEv4NevFDM'
                    #url = 'https://maps.googleapis.com/maps/api/directions/json?origin=12.9642,77.64442&destination=12.96269,77.64691&key=AIzaSyCOKScAM0z68czlcG7wxzbeQAEv4NevFDM'
                    try:
                        print url
                        r = requests.get(url)
                        if r.json()['status'] == 'ZERO_RESULTS':
                            print "No Directions found"
                        else:
                            value = r.json()['routes'][0]['legs'][0]['distance']['value']
                            matrix[count][i+1] = int(value)
                            matrix[i][count+1] = int(value)
                    except Exception as e:
                        print e
                    #matrix[count][i+1] = 1
                    #matrix[i][count+1] = 2
            count = count + 1
        print "After assign"
        print matrix

        matrix2 = matrix
        #remve the coloum
        matrix2 = scipy.delete(matrix2,0,1)
        matrix2 = matrix2.astype(int)

        #matrix = [[0,7693,6780,6885],[7693,0,2800,3881],[6780,2800,0,429],[6885,3881,429,0]]
        path,dis=tsp.fun(matrix2)

        print path,dis

        a = []
        count = 0
        for i in path:
            count = count + 1
            ClientList =  Clients.objects.get(name = matrix[path[i]][0])
            b = {
                "name" : ClientList.name,
                "lat" : ClientList.addressLatitude,
                "long" : ClientList.addressLogitude,
                "TripQueue" : count
            }
            a.append(b)

        return JsonResponse({'status' : "Success",'path' : path,'distance':dis,"pickups" : a})

def findsubsets(S,m):
    return set(itertools.combinations(S, m))