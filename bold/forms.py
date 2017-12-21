from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



class GenderPredictionForm(ModelForm):
    facebook = forms.BooleanField(initial=False, required=False)
    pinterest = forms.BooleanField(initial=False, required=False)
    pandora = forms.BooleanField(initial=False, required=False)
    espn = forms.BooleanField(initial=False, required=False, label='ESPN')
    linkedin = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = User
        fields = ['facebook', 'pinterest', 'linkedin', 'pandora', 'espn']


class MatchboxForm(ModelForm):
    facebook = forms.BooleanField(initial=False, required=False)
    instagram = forms.BooleanField(initial=False, required=False)
    drawsomething = forms.BooleanField(initial=False, required=False, label='Draw Something')
    templerun = forms.BooleanField(initial=False, required=False, label='Temple Run')
    clashofclans = forms.BooleanField(initial=False, required=False, label='Clash of Clans')
    wwffree = forms.BooleanField(initial=False, required=False, label='Words With Friends')
    pinterest = forms.BooleanField(initial=False, required=False)
    pandora = forms.BooleanField(initial=False, required=False)
    zombiefarm = forms.BooleanField(initial=False, required=False, label='Zombie Farm')


    class Meta:
        model = User
        fields = ['facebook', 'instagram', 'drawsomething', 'templerun', 'clashofclans', 'wwffree', 'pinterest', 'pandora', 'zombiefarm']

