from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

@csrf_exempt
def auth_login(req : HttpRequest):
    if req.method == 'POST' :
        code = -1

        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid(): 
            login(req, form.get_user())
            code = 1
        else : code = 0

    return JsonResponse({
        'code' : code
    })

@csrf_exempt
@login_required
def auth_logout(req : HttpRequest):
    logout(req)

    return JsonResponse({
        'code' : 1
    })