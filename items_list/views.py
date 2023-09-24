from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

@csrf_exempt
def get_list(req : HttpRequest):
    ...

@csrf_exempt
def get_categorys(req : HttpRequest):
    ...

#cars, house, animals, services, technologis