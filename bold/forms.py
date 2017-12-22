from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


choices = (
    ('15', 'Brigham Young University Food'), ('29', 'Texas Roadhouse'), ('418', 'BYU Legends Grille'), ('437', 'Brick Oven Provo'), ('516', 'The Wall - BYU'),
    ('693', 'Papa John\'s Pizza'), ('1365', 'Mountain West Burrito'), ('1401', 'Burgers Supreme'), ('1445', 'Chen\'s Noodle House'), ('374', 'Commons At The Cannon Center'),
    ('638', 'Panda Express'), ('695', 'NrGize'), ('4816', 'The Awful Waffle')
)

genders = (
    ('0', 'Female'), ('1', 'Male')
)

carriers = (
    ('Verizon', 'Verizon'), ('AT&T', 'AT&T'), ('Sprint', 'Sprint'), ('T-Mobile', 'T-Mobile')
)

users = (
    ('161', '161'), ('252', '252'), ('258', '258'), ('264', '264'), ('278', '278'), ('281', '281'), ('284', '284'), ('301', '301'), ('315', '315'), ('324', '324'),
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

    user_id = forms.ChoiceField(choices=users, required=False, label='User ID', help_text='Please select your User ID')
    facebook = forms.BooleanField(initial=False, required=False)
    instagram = forms.BooleanField(initial=False, required=False)
    drawsomething = forms.BooleanField(initial=False, required=False)
    templerun = forms.BooleanField(initial=False, required=False)
    clashofclans = forms.BooleanField(initial=False, required=False, label='Clash of Clans')
    wwffree = forms.BooleanField(initial=False, required=False, label='Words With Friends')
    pinterest = forms.BooleanField(initial=False, required=False)
    pandora = forms.BooleanField(initial=False, required=False)
    espn = forms.BooleanField(initial=False, required=False, label='ESPN')
    linkedin = forms.BooleanField(initial=False, required=False)
    twitter = forms.BooleanField(initial=False, required=False)
    netflix = forms.BooleanField(initial=False, required=False)
    groupon = forms.BooleanField(initial=False, required=False)
    newyorktimes = forms.BooleanField(initial=False, required=False, label='New York Times')
    gender = forms.ChoiceField(choices=genders, required=False, label='Gender')
    carrier = forms.ChoiceField(choices=carriers, required=False, label='Carrier')

    restaurant = forms.ChoiceField(choices=choices, required=False, label='Restaurant')
    visits = forms.IntegerField(min_value=0, label='Number of visits during the semester:')


    class Meta:
        model = User
        fields = [ 'facebook','instagram', 'drawsomething','templerun', 'clashofclans','wwffree', 'pinterest','pandora', 'linkedin','twitter', 'netflix', 'groupon', 'newyorktimes', 'espn','user_id', 'gender','carrier', 'restaurant', 'visits']

