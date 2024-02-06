from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import LikePost
from .models import Like

from registration.models import UserModel
from items_list.models import Item

class LikeView(APIView) :
    def post(req : HttpRequest):
        code = -1

        print(req.user.is_authenticated)
        
        if req.method == 'POST' :
            item_like_form = LikePost(req.POST)
    
            if item_like_form.is_valid():
                data = req.POST.dict()
                
                user = UserModel.objects.get(id = req.user.id)
                item = Item.objects.get(id = data['item_id'])
                
                print(item)

                liked_post = Like(user, item)
                    
                if data.get('like') == 1:
                    liked_post.save()
                elif data.get('like') == 0 and liked_post.objects.exists():                
                    liked_post.delete()
                
                code = 1
                
            else : 
                print(item_like_form.errors)
                code = 0

        return Response({'code' : code})