from django import forms
from django.contrib.auth import authenticate
from .models import Internship, Scholarship
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            #basic info
            'title', 'field', 'pos', 'desc',
            #time & location
            'valid_date', 'city', 'state',
            #edu requirements
            'edu_level','degree',
            #financial info
            'amount'
        ]
        widgets = {
            'valid_date': DatePickerInput(format='%Y-%m-%d'), 
            'date_posted': DatePickerInput(format='%Y-%m-%d'),
        }

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = [
            #basic info
            'title', 'field', 'pos', 'desc',
            #time & location
            'valid_date', 'city', 'state',
            #edu requirements
            'edu_level','degree',
            #financial info
            'amount'
        ]
        widgets = {
            'valid_date': DatePickerInput(format='%Y-%m-%d'), 
            'date_posted': DatePickerInput(format='%Y-%m-%d'),
        }