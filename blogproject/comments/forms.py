from django import forms
from .models import Comment, Contact

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'url', 'email', 'text']


class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']