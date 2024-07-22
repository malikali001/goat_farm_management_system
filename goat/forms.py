from django import forms

from base.models.goats import Goat


class GoatForm(forms.ModelForm):
    class Meta:
        model = Goat
        fields = ['name', 'breed', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
        }
