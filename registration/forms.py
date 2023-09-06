from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

import re

class phone_form(forms.Form):
    phone = forms.CharField(max_length=13, min_length=10)

class email_form(forms.Form):
    email = forms.EmailField(max_length=35)

class user_private(forms.Form):
    username = forms.CharField(min_length=8, max_length=25)
    password = forms.CharField(min_length=9)

    def has_special_char(self, s):
        for c in s:
            if not (c.isalpha() or c.isdigit() or c == ' '):
                return True
        return False

    def clean_password(self) :
        data = self.cleaned_data['password']

        digit_contains = any(str(char).isdigit() for char in data)

        islower_contains = any(str(char).islower() for char in data)

        isupper_contains = any(str(char).isupper() for char in data)

        special_contains = self.has_special_char(data)

        if digit_contains and islower_contains and isupper_contains and special_contains :
            return data
        else : raise ValidationError('Invalid password type')

class user_data_form(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=35)
    phone = forms.CharField(max_length=13, min_length=10)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
