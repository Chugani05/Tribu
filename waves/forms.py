from django import forms
from .models import Wave

class AddWaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)
