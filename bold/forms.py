from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



class GenderPredictionForm(ModelForm):
    facebook = forms.BooleanField(help_text='Facebook', initial=False, required=False)
    pinterest = forms.BooleanField(help_text='Pinterest', initial=False, required=False)
    pandora = forms.BooleanField(help_text='Pandora', initial=False, required=False)
    espn = forms.BooleanField(help_text='ESPN', initial=False, required=False)
    linkedin = forms.BooleanField(help_text='Linkedin', initial=False, required=False)

    class Meta:
        model = User
        fields = ['facebook', 'pinterest', 'pandora', 'espn', 'linkedin']
