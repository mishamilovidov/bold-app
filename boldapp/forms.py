from django.forms import ModelForm, formset_factory
from boldapp.models import User, Equipment, Department, Manufacturer
from django import forms
import datetime

from django.forms import BaseFormSet, BaseModelFormSet, ValidationError


EQUIP_TYPES = (
    ('laptop', 'Laptop'), ('desktop', 'Desktop'), ('tablet', 'Tablet')
)

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']


class EquipmentForm(ModelForm):

    name = forms.CharField(max_length=100, label='Name')
    organizationaltag = forms.CharField(max_length=100, label='Organizational Tag')
    description = forms.CharField(max_length=100, label='Description')
    type = forms.ChoiceField(choices=EQUIP_TYPES, label='Equipment Type')
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.order_by('name').all(), label='Manufacturer', empty_label=None)
    manufacturerpartnum = forms.CharField(max_length=100, label='Part Number')
    department = forms.ModelChoiceField(queryset=Department.objects.order_by('name').all(), label='Department', empty_label=None)
    officelocation = forms.CharField(max_length=100, label='Office Location')
    user = forms.ModelChoiceField(queryset=User.objects.only('username'), label='User', empty_label=None)

    class Meta:
        model = Equipment
        fields = ['name', 'organizationaltag', 'description', 'type', 'manufacturer', 'manufacturerpartnum', 'department', 'officelocation', 'user']


class ManufacturerForm(ModelForm):
    name = forms.CharField(max_length=100, label='Name')
    accountnumber = forms.CharField(max_length=100, label='Account Number')
    accountmanager = forms.CharField(max_length=100, label='Account Manager')
    supportnumber = forms.CharField(max_length=100, label='Support Number')

    class Meta:
        model = Equipment
        fields = ['name', 'accountnumber', 'accountmanager', 'supportnumber']


class DepartmentForm(ModelForm):
    name = forms.CharField(max_length=100, label='Name')
    supervisor = forms.CharField(max_length=100, label='Supervisor')
    phonenumber = forms.CharField(max_length=100, label='Phone Number')

    class Meta:
        model = Equipment
        fields = ['name', 'supervisor', 'phonenumber']
