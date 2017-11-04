from django import forms
from .models import Importer


class ImporterForm(forms.ModelForm):
    class Meta:
        model = Importer
        fields = ['name', ]
