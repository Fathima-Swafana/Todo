from .models import Demmy
from django import forms


class DemmyForm(forms.ModelForm):
    class Meta:
        model = Demmy
        fields = ['name', 'priority', 'date']
