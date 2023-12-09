from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import LikePost

from .models import Like
# from registration.models import UserModel
from items_list.models import Item

@csrf_exempt
def post_like(req : HttpRequest):
    # code = -1

    # print(req.user.is_authenticated)
    
    # if req.method == 'POST' :
    #     item_like_form = LikePost(req.POST)
 
    #     if item_like_form.is_valid():
    #         data = req.POST.dict()
            
    #         user = UserModel.objects.get(id = req.user.id)
    #         item = Item.objects.get(id = data['item_id'])
            
    #         print(item)

    #         liked_post = Like(user, item)
                
    #         if data.get('like') == 1:
    #             liked_post.save()
    #         elif data.get('like') == 0 and liked_post.objects.exists():                
    #             liked_post.delete()
            
    #         code = 1
            
    #     else : 
    #         print(item_like_form.errors)
    #         code = 0

    # return JsonResponse({'code' : code})
    return JsonResponse({'code' : 1})