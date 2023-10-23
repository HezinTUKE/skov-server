from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils import timezone

from registration.models import UserModel
from .models import CategoryLang, SubCategory, PartnerItem, Item, PhotoItem

from locations.models import Country, Regions
from .forms import GetItemForm, CreateitemForm


@csrf_exempt
def get_list(req : HttpRequest):
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

        return JsonResponse({
            'items' : vals
        })

@csrf_exempt
def get_item(req : HttpRequest):
    if req.method == 'GET' :
        data = req.GET.dict()
        form = GetItemForm(req.GET)

        if form.is_valid() :
            item = Item.objects.get(id = data['id'])

            owner = UserModel.objects.get(username = item.owner)

            my_item = req.user.id == owner.id

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
                'my_item' : my_item,
            }

            if my_item :
                val['is_active'] = item.is_active
                if not item.is_active:
                    val['active_time'] = item.active_time 

            return JsonResponse({
                'item' : val
            })

        else :
            return JsonResponse({'item' : None})

@csrf_exempt
def create_item(req : HttpRequest) :
    if req.method == 'POST' :
        if req.user.is_active :
            
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

                return JsonResponse({'code' : 1})
            else :
                print(item_form.errors)
                return JsonResponse({'code' : -1})
        
        else : return JsonResponse({'code' : 0})

@csrf_exempt
def get_categorys(req : HttpRequest):
    ...

#cars, house, animals, services, technologis