from django import forms
from base.models.healths import Health


class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ['date', 'title', 'description', 'treatment', 'goat']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'treatment': forms.TextInput(attrs={'class': 'form-control'}),
            'goat': forms.Select(attrs={'class': 'form-control'}),
        }
