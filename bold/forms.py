from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


choices = (
    ('15', 'Brigham Young University Food'), ('29', 'Texas Roadhouse'), ('418', 'BYU Legends Grille'), ('437', 'Brick Oven Provo'), ('516', 'The Wall - BYU'),
    ('693', 'Papa John\'s Pizza'), ('1365', 'Mountain West Burrito'), ('1401', 'Burgers Supreme'), ('1445', 'Chen\'s Noodle House'), ('374', 'Commons At The Cannon Center'),
    ('638', 'Panda Express'), ('695', 'NrGize'), ('4816', 'The Awful Waffle')
)




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

    restaurant = forms.ChoiceField(choices=choices, required=False, label='Restaurant')
    visits = forms.IntegerField(min_value=0, label='Number of visits during the semester:')


    class Meta:
        model = User
        fields = ['restaurant', 'visits']

