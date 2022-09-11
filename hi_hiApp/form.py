from django.db.models.base import Model
from .models import *
from django import forms
from django.db import models
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class signupForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':('Username')}),)
    names = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder':('names')}), )
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder':('email')}),)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Phone Number')}),
        label= ("Phone number"),required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
            )

    def save(self, commit = True):
        user = super(signupForm,self).save(commit = False)
        user.phone_number = self.cleaned_data['phone_number']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
        
class sending_moneyForm(ModelForm):
    user = forms.CharField(max_length=30)
    class Meta:
        model = transaction
        fields = ('user', 
                  'Currency', 
                  'amount'
                )
    
class top_upForm(ModelForm):
    class Meta:
        model = users_wallet
        fields = (
            # 'user',
            'credict_ballance',
            'Currency',
            'Billing_Address',
        )