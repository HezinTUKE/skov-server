from django.http import HttpRequest
from django.contrib.sessions.backends.db import SessionStore

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import string
import random

from datetime import datetime, timedelta
from .forms import *
from .models import *

session = SessionStore()

session.set_expiry(
    timedelta(minutes=15)
)

class RegistrationPhoneStepView(APIView) :

    permission_classes = [AllowAny]

    def post(self, req : HttpRequest) :
        if req.method == 'POST' : 
            form = phone_form(req.POST)
            code = -1

            print(req.POST.dict().get('phone'))

            if form.is_valid() :
                phone = UserModel.objects.filter(phone = req.POST.dict().get('phone')).first()

                if phone :
                    code = -2
                else :          

                    session['secret'] = ''.join(random.choices(
                        string.ascii_uppercase + string.digits,
                        k=5
                    ))     

                    session['sms_active'] = False

                    if session.modified :
                        print(session['secret'])
                        session.save()

                    code = 1

            return Response(
                { 
                    'code' : code
                }
            )

class RegistrationSMSStepView(APIView) :
    permission_classes = [AllowAny]

    def post(self, req : HttpRequest) :
        if req.method == 'POST' :
            code = -1
            secret = req.POST.dict().get('secret')

            print(session.items())

            if session.get('secret') == None :
                code = -1
            elif session.get('secret') == secret.upper():
                del session['secret']
                session['sms_active'] = True

                code = 1

            return Response(
                {
                    'code' : code
                }
            )

class RegistrationValidEMail(APIView) :
    permission_classes = [AllowAny]

    def get(req : HttpRequest) : 
        if req.method == 'GET' :
            ...

    def post(req : HttpRequest) :
        if req.method == 'POST' :
            ...

class RegistrationPasswordStep(APIView) :
    permission_classes = [AllowAny]

    def post(self, req : HttpRequest) :
        if req.method == 'POST' :
            data = req.POST
            print(data.dict())
            code = -1

            form_private =  user_private(data)

            if form_private.is_valid() :
                user = UserModel.objects.filter(username = data.dict().get('username'))

                if user :
                    code = -2
                else :
                    code = 1
            else : 
                print(form_private.errors)

            return Response( 
                {
                    'code' : code
                }
            )              

class CreateUserView(APIView) :
    permission_classes = [AllowAny]

    def post(self, req : HttpRequest) :
        if req.method == 'POST' :
            data = req.POST
            code = -1
            form_res = user_data_form(data)

            if form_res.is_valid() and session['sms_active']:
                date = datetime.strptime(data['date_of_birth'], '%d.%m.%Y').strftime('%Y-%m-%d')

                usr = UserModel.objects.create_user(
                    username=data['username'],
                    password=data['password'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    phone=data['phone'],
                    date_of_birth=date
                )

                usr.save()

                code = 1
            else :
                print("WRONG")
                print(form_res.errors)

            return Response(
                {
                    'code' : code
                }
            )
