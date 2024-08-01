from django import forms
from .models import Guess

class NumberForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields = ('guess',)
        widgets = {
            'guess': forms.TextInput(attrs={'class': 'form-control'}),
        }
