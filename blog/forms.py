from django import forms
from .models import *
from tinymce.widgets import TinyMCE


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'image', )


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
        }


class NewsLetterForm(forms.Form):
    subject = forms.CharField()
    recievers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label='Email Content')
