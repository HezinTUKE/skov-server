from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Icon
from .forms import IconForm

class IconView(APIView) :
    permission_classes = [IsAdminUser]

    def post(self, req : HttpRequest):
        code = -1
        icon_form = IconForm(req.POST, req.FILES)
        print(req.FILES)
        if icon_form.is_valid() :

            icon = Icon(
                        name = req.POST.dict()['name'], 
                        icon = req.FILES['icon']
                    )
            
            icon.save()
            code = 1
        else :
            print(icon_form.errors)

        return Response({
            'code' : code
        })