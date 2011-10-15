from django import forms
from models import Palestrante

class Test(forms.Form):
    nome = forms.CharField(label='Nome da pessoa')
    nome1 = forms.CharField(label='Nome da pessoa')
    nome2 = forms.CharField(label='Nome da pessoa')
    nome3 = forms.CharField(label='Nome da pessoa')
    nome4 = forms.CharField(label='Nome da pessoa')
















class PalestranteForm(forms.ModelForm):
    class Meta:
        model = Palestrante









