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
        icon_form = IconForm(req.FILES)
        if icon_form.is_valid() :
            icon = Icon(req.FILES['icon'])
            icon.save()
            code = 1
        
        return Response({
            'code' : code
        })