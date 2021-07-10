from django import forms
from django.db import models
from django.forms import ModelForm, fields
from .models import Profile

#create a profile form for website
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        #to call all fields
        #fields = "__all__"
        #to call needed fields only
        fields = ('Name', 'Address', 'Age', 'Sex', 'Education', 'Occupation', 'Hight', 'Weight', 'Mobile_no', 'Diocese', 'Parish', 'Community', 'Town', 'Family_Status', 'Name_of_the_Parent', 'Parent_mobile', 'Partners_Requirements', 'Contact_address', 'Office_use', 'Place', 'date')
