from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name','username','phone_number','password1','password2')

        labels = {
            'first_name':'',
            'last_name': '',
            'username': '',
            'phone_number': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'required':'', 'placeholder':'First name'}),
            'last_name': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'required':'', 'placeholder':'Last name'}),
            'username': forms.TextInput(attrs={'type':'text', 'class':'form-control','required':'', 'placeholder':'Username'}),
            'phone_number': forms.NumberInput(attrs={'type':"number", 'class':"form-control", 'required':'', 'placeholder':'Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password confirmation'