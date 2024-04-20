# forms.py

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_details', 'skills', 'extracurricular_activities', 'education', 'other_information']
