from django import forms
from .models import contact
from django.forms import ModelForm, Textarea
class ContactForm(forms.ModelForm):
    name = forms.CharField(label=' Your name', max_length=100,required=True)
    email = forms.EmailField(label='Your email', max_length=100,required=True)
    phone = forms.CharField(label='Your phone number', max_length=10, required=True)
    comment = forms.CharField(label='Additional comments', max_length=500,required=True,widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

    class Meta:
        model = contact
        fields=('name','email','comment','phone',)

