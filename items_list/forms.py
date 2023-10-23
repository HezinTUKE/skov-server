from django import forms

class GetItemForm(forms.Form):
    id = forms.IntegerField()

class CreateitemForm(forms.Form):
    category_id = forms.IntegerField()
    subcategory_id = forms.IntegerField()
    is_active = forms.BooleanField()
    title = forms.CharField(min_length=5, max_length=15)
    price = forms.FloatField(max_value=1_000_000)
    description = forms.CharField(max_length=255)
    photos = forms.ImageField()
    country_id = forms.IntegerField()
    region_id = forms.IntegerField()
    district_id = forms.IntegerField(required=False)