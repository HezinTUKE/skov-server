from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore
from .models import UserModel
from datetime import datetime, timedelta
import string
import random

from .forms import *
from .models import *


session = SessionStore()

session.set_expiry(
    timedelta(minutes=15)
)

@csrf_exempt
def get_phone(req : HttpRequest) :
    if req.method == 'POST' : 
        form = phone_form(req.POST)
        code = -1

        print(req.POST.dict().get('phone'))

        if form.is_valid() :
            phone = UserModel.objects.filter(phone = req.POST.dict().get('phone')).first()

            if phone :
                code = -2
            else :
                secret = ''.join(random.choices(
                    string.ascii_uppercase + string.digits,
                    k=5
                ))            
                
                print(secret)

                session['secret'] = secret
                session['sms_active'] = False

                code = 1

        return JsonResponse(
            { 
                'code' : code
            }
        )
    
@csrf_exempt
def check_sms(req : HttpRequest) :
    if req.method == 'POST' :
        code = -1
        secret = req.POST.dict().get('secret')

        if session.get('secret') == None :
            code = -1
        elif session.get('secret') == secret.upper():
            del session['secret']
            session['sms_active'] = True

            code = 1

        return JsonResponse(
            {
                'code' : code
            }
        )

def get_email(req : HttpRequest) : 
    if req.method == 'POST' :
        ...

def send_email(req : HttpRequest) :
    if req.method == 'GET' :
        ...

@csrf_exempt
def get_user_private(req : HttpRequest) :
    if req.method == 'POST' :
        data = req.POST
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

        return JsonResponse( 
            {
                'code' : code
            }
        )              

@csrf_exempt
def get_user_data(req : HttpRequest) :
    if req.method == 'POST' :
        data = req.POST
        code = -1
        form_res = user_data_form(data)

        if form_res.is_valid() and session['sms_active']:
            print("Hello ok")

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

        return JsonResponse(
            {
                'code' : code
            }
        )
