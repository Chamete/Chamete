""" from socket import fromshare """
from django import forms
from .models import Libro
from django import forms

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'


