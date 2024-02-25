from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class LoginView(APIView) :
    
    authentication_classes = [TokenAuthentication]

    def post(self, req : HttpRequest):
        code = -1
        token = ''
        if req.method == 'POST' :
            data = req.POST.dict()  
            form = authenticate(req, username=data['username'], password=data['password'])
            
            if form is not None: 
                login(req, form)
                req.session.modified = True
                
                token = Token.objects.get(user = form)
                token = token.key
                code = 1
                
            else : code = 0

        return Response({
            'token' : token,
            'code' : code
        })
    


class LogoutView(APIView) :

    permission_classes = [IsAuthenticated]

    def post(self, req : HttpRequest):
        logout(req)

        return JsonResponse({
            'code' : 1
        })