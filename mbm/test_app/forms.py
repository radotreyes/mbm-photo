from django import forms
from . import models
from django.contrib.auth.models import User
from django.core import validators

def check_for_z( value ):
    if value[0].lower() != 'z':
        raise forms.ValidationError( "Name needs to start with Z!" )

class UserAuthForm( forms.ModelForm ):
    password = forms.CharField( widget = forms.PasswordInput() )

    class Meta():
        model = models.User
        fields = ( 'username', 'password' )

class ImageUploadForm( forms.ModelForm ):

    class Meta():
        model = models.ImageUpload
        fields = '__all__'
