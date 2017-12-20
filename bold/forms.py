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
