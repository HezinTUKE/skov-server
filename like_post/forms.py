from django import forms

class LikePost(forms.Form):
    like = forms.IntegerField(required=True)
    item_id = forms.IntegerField(required=True)