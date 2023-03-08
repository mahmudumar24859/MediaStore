from django import forms
from django.forms import ModelForm
from .models import *


class AudioUpload(forms.ModelForm):
    class Meta:
        model = SahihMuslim
        fields = ('title', 'artist', 'audio_file')

        labels = {
            'title': '',
            'artist': '',
            'audio_file': 'Audio File',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Audio Title'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Sheikh'}),
        }
