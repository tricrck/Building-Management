from django import forms

from .models import Building, Apartment, Tenant


class BuildingModelForm(forms.ModelForm):
    class Meta:
        model = Building
        fields =[
            'Number',
            'Street',
        ]
class ApartmentModelForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields =[
            'Number',
            'Monthly_rent',
            'Building',
        ]

class TenantModelForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields =[
            'First_name',
            'Last_name',
            'Age',
            'Gender',
            'Apartment',
            

        ]