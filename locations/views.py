from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Country, Regions, Districts

class CountryView(APIView) :

    authentication_classes = [AllowAny]

    def get(req : HttpRequest):
        if req.method == 'GET' :
            countrys = Country.objects.all().values('id','country')    

            vals = [ 
                {'id' : i['id'], 'name' : i['country']} for i in countrys
            ]

            return Response({'countrys' : vals})
    
class RegionView(APIView) :
    
    authentication_classes = [AllowAny]

    def get(req : HttpRequest):
        if req.method == 'GET' :
            data = req.GET.dict()

            country_id = data['country_id']

            if country_id == -1 :
                return Response({})
            else :
                regions = Regions.objects.filter(coutry_id = country_id).values('id', 'region')

                vals = [
                    {'id' : i['id'], 'name' : i['region']} for i in regions
                ]

                return Response({'regions' : vals})
        
class DistrictView(APIView):
    
    authentication_classes = [AllowAny]

    def get(req : HttpRequest):
        if req.method == 'GET' :
            data = req.GET.dict()

            reg_id = data['region_id']

            if reg_id == -1 :
                return Response({})
            else : 
                districts = Districts.objects.filter(region_id = reg_id).values('id', 'district')

                vals = [
                    {'id' : i['id'], 'name' : i['district']} for i in districts
                ]

                return Response({'districts' : vals})
        