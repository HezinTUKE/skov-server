from django import forms

class IconForm(forms.Form):
    icon = forms.ImageField()