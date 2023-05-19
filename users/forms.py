from django import forms
from django.forms import TextInput, Select, DateInput, BooleanField,Textarea

from users.models import Customer


class CustomerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "input","type": "text"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "input","type": "password"}))
    class Meta:
        model = Customer
        exclude = ('user', 'is_deleted')

        widgets = {
            'phone_no': TextInput(attrs={'class': "input","type": "text"}),
            'name': TextInput(attrs={'class': "input","type": "text"}),
            'email': TextInput(attrs={'class': "input","type": "text"}),
            'address': Textarea(attrs={'class': "input", 'rows':5,"type": "text"}),
            'date_of_birth': DateInput(attrs={"type": "date", 'style':"background:#fff;color:#000"}),
            
        }