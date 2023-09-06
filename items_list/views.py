from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_list(req : HttpRequest):
    ...