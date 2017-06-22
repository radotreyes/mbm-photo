from django import forms
from test_app.models import Topic, Webpage, AccessRecord, UserProfile
from django.contrib.auth.models import User
from django.core import validators

def check_for_z( value ):
    if value[0].lower() != 'z':
        raise forms.ValidationError( "Name needs to start with Z!" )

class UserAuthForm( forms.ModelForm ):
    password = forms.CharField( widget = forms.PasswordInput() )

    class Meta():
        model = User
        fields = ( 'username', 'email', 'password' )

class UserProfileForm( forms.ModelForm ):
    website = forms.URLField( required = False )
    picture = forms.ImageField( required = False )

    class Meta:
        model = UserProfile
        exclude = ( 'user', )
