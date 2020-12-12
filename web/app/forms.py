from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)





class CustomUserChangeForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)