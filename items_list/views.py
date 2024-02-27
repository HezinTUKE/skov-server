from django.http import HttpRequest
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CategoryLang, SubCategory, Item, PhotoItem
from .forms import GetItemForm, CreateitemForm

from registration.models import UserModel
from like_post.models import Like
from locations.models import Country, Regions

class ItemsListView(APIView) : 
    
    permission_classes = [IsAuthenticated]

    def get(self, req : HttpRequest):
        if req.method == 'GET' :
            items = Item.objects.filter(
                is_active = True
            ).order_by('-active_time')
            
            vals = [
                {
                    'id' : item.id,
                    'title' : item.title,
                    'price' : "{:.2f}".format(item.price),
                    'category' : CategoryLang.objects.get(id = item.category_id).name_en,
                    'subcategory' : SubCategory.objects.get(id = item.subcategory_id).name_en,
                    'country' : Country.objects.get(id = item.country_id).short,
                    'region' : Regions.objects.get(id = item.region_id).region,
                    'photos' : [ i[1] for i in item.photos.values_list() ]
                } for item in items
            ]

            return Response({
                'items' : vals
            })

class ItemView(APIView) :
    
    permission_classes = [IsAuthenticated]

    def get(self, req : HttpRequest):
        if req.method == 'GET' :
            data = req.GET.dict()
            form = GetItemForm(req.GET)

            if form.is_valid() :
                item = Item.objects.get(id = data['id'])

                owner = UserModel.objects.get(username = item.user)

                my_item = req.user.id == owner.id

                is_liked_post = Like.objects.filter(user = req.user.id).exists()

                val = {
                    'id' : data['id'],
                    'title' : item.title,
                    'price' : "{:.2f}".format(item.price),
                    'description' : item.description,
                    'category' : CategoryLang.objects.get(id = item.category_id).name_en,
                    'subcategory' : SubCategory.objects.get(id = item.subcategory_id).name_en,
                    'country' : Country.objects.get(id = item.country_id).country,
                    'region' : Regions.objects.get(id = item.region_id).region,
                    'photos' : [ i[1] for i in item.photos.values_list() ],
                    'is_owner' : my_item,
                    'is_liked' : is_liked_post
                }

                if my_item :
                    val['is_active'] = item.is_active
                    if not item.is_active:
                        val['active_time'] = item.active_time 

                return Response({
                    'item' : val
                })

            else :
                return Response({'item' : None})

    def post(self, req : HttpRequest) :
        if req.method == 'POST' :
            item_form = CreateitemForm(req.POST, req.FILES)
            if item_form.is_valid() :
                data = req.POST.dict()

                is_active = data['is_active']
                time = timezone.now()

                item = Item(
                        owner = UserModel.objects.get(id = req.user.id),
                        category = CategoryLang.objects.get(id = data['category_id']),
                        subcategory = SubCategory.objects.get(id = data['subcategory_id']),
                        is_active = is_active,
                        title = data['title'],
                        price = data['price'],
                        description = data['description'], 
                        create_time = time,
                        country = Country.objects.get(id = data['country_id']),
                        region = Regions.objects.get(id = data['region_id'])
                    )
                
                if data.get('district_id') :
                    item.district = data['district_id']
                
                if is_active :
                    item.active_time = time
                elif data.get('active_time') :
                    item.active_time = data['active_time']

                item.save()
                
                for i in req.FILES.getlist('photos') :
                    photo = PhotoItem.objects.create(
                        image = i
                    )

                    photo.save()

                    item.photos.add(photo)

                return Response({'code' : 1})
            else :
                print(item_form.errors)
                return Response({'code' : -1})
            
        else :
                return Response({'code' : 0})
        
class CategoryView(APIView) :
    permission_classes = [AllowAny]

    def get(self, req : HttpRequest) :
        if req.method == 'GET' :
            category = CategoryLang.objects.all().values('id', 'name_sk')

            res = [
                {'id' : i['id'], 'name' : i['name_sk']} for i in category
            ]

            return Response({
                'categorys' : res 
            })

class SubCategoryView(APIView) :
    permission_classes = [AllowAny]

    def get(self, req : HttpRequest) :
        if req.method == 'GET' :
            data = req.GET.dict()
            subcategory = SubCategory.objects.filter(category_id = data['category']).values('id', 'name_sk')

            res = [
                {'id' : i['id'], 'name' : i['name_sk']} for i in subcategory
            ]

            return Response({
                'subcategorys' : res 
            })