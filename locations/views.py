from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from icons.models import Icon

from .models import Country, Regions, Districts

class CountryView(APIView) :

    permission_classes = [AllowAny]

    def get(self, req : HttpRequest):
            countrys = Country.objects.all().values('id','country','icon')    

            vals = [ 
                {'id' : i['id'], 'name' : i['country'], 'icon' : str( Icon.objects.get(id = i['icon']).icon ) } 
                    for i in countrys
            ]

            # for d in vals :
            #     for k, v in d.items():
            #         if k == 'icon' :
            #             i = Icon.objects.get(id = v)
            #             d[k] = str(i.icon)

            return Response({'location' : vals})
    
class RegionView(APIView) :
    
    permission_classes = [AllowAny]

    def get(self, req : HttpRequest):
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

                return Response({'location' : vals})
        
class DistrictView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, req : HttpRequest):
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

                return Response({'location' : vals})
        