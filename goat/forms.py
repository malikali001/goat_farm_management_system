from django import forms

from base.models.goats import Goat


class GoatForm(forms.ModelForm):
    class Meta:
        model = Goat
        fields = ['name', 'breed', 'date_of_birth', 'manager']
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'datepicker'}),
        }
