from django import forms
from test_app.models import Topic, Webpage, AccessRecord, User
from django.core import validators

def check_for_z( value ):
    if value[0].lower() != 'z':
        raise forms.ValidationError( "Name needs to start with Z!" )

class FormNameEmailMsg( forms.ModelForm ):
    class Meta:
        model = User
        fields = '__all__'
