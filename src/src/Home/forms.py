from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from src.Home import models


class RegistrationForm(UserCreationForm):
    #Adding email field
    email = forms.EmailField(required=True)
#Updating our user model to include email
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
    )
    def save(self, commit=True):
        #cleaned data makes sure any data entered isn't malicious
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
