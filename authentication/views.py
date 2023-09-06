from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from registration.models import UserModel

@csrf_exempt
def auth_login(req : HttpRequest):
    data = req.POST.dict()
    code = -1

    if 'username' in data : 
        auth_user = authenticate(req, username = data.get('username'), password = data.get('password'))

        if auth_user is not None:
            login(req, auth_user)
            code = 1

    return JsonResponse({
        'code' : code
    })

@csrf_exempt
def logout(req : HttpRequest):
    code = -1

    logout(req)

    return JsonResponse({
        'code' : code
    })