from django import forms
from . import models
from django.contrib.auth.models import User
from django.core import validators

class UserAuthForm( forms.ModelForm ):
    password = forms.CharField( widget = forms.PasswordInput() )

    class Meta():
        model = models.User
        fields = ( 'username', 'password' )

class ImageUploadForm( forms.ModelForm ):

    class Meta():
        model = models.ImageUpload
        fields = '__all__'
