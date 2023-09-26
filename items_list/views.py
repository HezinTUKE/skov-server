from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Item, CategoryLang, SubCategory, PhotoItem
from registration.models import UserModel
from locations.models import Country, Regions

from .forms import GetItemForm

@csrf_exempt
def get_list(req : HttpRequest):
    if req.method == 'GET' :
        items = Item.objects.filter(
                is_active = True
            ).values(
                'id', 'title', 'category', 'subcategory', 'country', 'region', 'description', 'price'
            )

        vals = [
            {
                'id' : item['id'],
                'title' : item['title'],
                'description' : item['description'],
                'price' : item['price'],
                'category' : CategoryLang.objects.get(id = item['category']).name_en,
                'subcategory' : SubCategory.objects.get(id = item['subcategory']).name_en,
                'country' : Country.objects.get(id = item['country']),
                'region' : Regions.objects.get(id = item['region']),
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

            owner = UserModel.objects.get(id = item['owner'])

            my_item = req.user.id == owner.id

            val = {
                'id' : data['id'],
                'owner' : owner,
                'title' : item['title'],
                'price' : item['price'],
                'description' : item['description'],
                'category' : CategoryLang.objects.get(id = item['category']).name_en,
                'subcategory' : SubCategory.objects.get(id = item['subcategory']).name_en,
                'country' : Country.objects.get(id = item['country']),
                'region' : Regions.objects.get(id = item['region']),
                'my_item' : my_item
            }

            if my_item :
                val['is_active'] = item['is_active']
                val['active_time'] = item['active_time']

            return JsonResponse({
                'item' : val
            })

        else :
            return JsonResponse({'item' : None})

@csrf_exempt
def create_item(req : HttpRequest) :
    def get_name():
        from datetime import datetime
        now = datetime.utcnow()

        str_now = now.strftime("%Y%m%d_%H%M%S%f")[:-3]

        name = f"{str_now}.jpg"

        return name

    if req.method == 'POST' :
        data = req.POST.dict()

        item = Item(
                owner = UserModel.objects.get(id = req.user.id),
                category = CategoryLang.objects.get(id = data['category_id']),
                subcategory = SubCategory.objects.get(id = data['subcategory_id']),
                is_active = data['is_active'],
                title = data['title'],
                price = data['price'],
                description = data['description'] 
            )

        if data.get('country') :
            item.country = data['country']
        if data.get('region') :
            item.region = data['region']
        if data.get('district') :
            item.district = data['district']

        item.save()
        
        for i in req.FILES.values() :
            print(get_name())
            photo = PhotoItem.objects.create(
                image = i,
                name = get_name()
            )

            photo.save()

            item.photos.add(photo)

        return JsonResponse({'code' : 1})

@csrf_exempt
def get_categorys(req : HttpRequest):
    ...

#cars, house, animals, services, technologis