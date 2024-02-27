from django import forms

class IconForm(forms.Form):
    name = forms.CharField(max_length=25)
    icon = forms.ImageField()