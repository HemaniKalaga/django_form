from typing import Any
from django import forms 
from app.models import *
from django.core import validators
import re

def validate_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('It should not be started with numerics')
    
def validate_nume(data):
    if re.match('^[0-9]',data):
        raise forms.ValidationError('Numerics should not be given')

def validate_z(data):
    if data.lower().startswith('z'):
        raise forms.ValidationError('It should not startwith Z or z')



class Topic_form(forms.Form):
    topic_name=forms.CharField()

class Webpage_form(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField(validators=[validate_a,validate_z,validate_nume,validators.RegexValidator('')])
    url=forms.URLField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        email=self.cleaned_data['email']
        re_enter_email=self.cleaned_data['re_enter_email']
        if email != re_enter_email:
            raise forms.ValidationError('Emails are not matching')     

    def clean_botcatcher(self):
        b=self.cleaned_data('botcatcher')
        if len(b) > 0:
            raise forms.ValidationError('invalid')


class AccessRecord_form(forms.Form):
    wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    date=forms.DateField()
    author=forms.CharField()

    