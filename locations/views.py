from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Country, Regions, Districts


@csrf_exempt
def get_country(req : HttpRequest):
    if req.method == 'GET' :
        countrys = Country.objects.all().values('id','country')    

        vals = [ 
            {'id' : i['id'], 'name' : i['country']} for i in countrys
        ]

        return JsonResponse({'countrys' : vals})
    
@csrf_exempt
def get_regions(req : HttpRequest):
    if req.method == 'GET' :
        data = req.GET.dict()

        country_id = data['id']

        if country_id == -1 :
            return JsonResponse({})
        else :
            regions = Regions.objects.filter(coutry_id = country_id).values('id', 'region')

            vals = [
                {'id' : i['id'], 'name' : i['region']} for i in regions
            ]

            return JsonResponse({'regions' : vals})
        
@csrf_exempt
def get_districts(req : HttpRequest):
    if req.method == 'GET' :
        data = req.GET.dict()

        reg_id = data['id']

        if reg_id == -1 :
            return JsonResponse({})
        else : 
            districts = Districts.objects.filter(region_id = reg_id).values('id', 'district')

            vals = [
                {'id' : i['id'], 'name' : i['district']} for i in districts
            ]

            return JsonResponse({'districts' : vals})
        