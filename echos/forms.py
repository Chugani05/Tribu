from django import forms
from .models import Echo

class AddEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)

    def __init__(self, user, *args, **kargs):
        super().__init__(*args, **kargs)
        self.user = user

    def save()