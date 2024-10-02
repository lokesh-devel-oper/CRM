from django import forms
from .models import LEAD

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = LEAD
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

class Leadform(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)