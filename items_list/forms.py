from django import forms

class GetItemForm(forms.Form):
    id = forms.IntegerField()