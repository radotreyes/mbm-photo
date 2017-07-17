from django import forms
from . import models
from django.contrib.auth.models import User
from django.core import validators

class BootstrapModelForm( forms.ModelForm ):
    def __init__( self, *args, **kwargs ):
        super( BootstrapModelForm, self ).__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            })

class UserAuthForm( forms.ModelForm ):
    password = forms.CharField( widget = forms.PasswordInput() )

    class Meta():
        model = models.User
        fields = ( 'username', 'password' )

class EmailForm( BootstrapModelForm ):
    class Meta():
        model = models.EmailRequest
        fields = '__all__'

    def __init__( self, *args, **kwargs ):
        '''
        This use of __init__ changes how Django renders forms which are called with template tags.
        '''
        super( EmailForm, self ).__init__(*args, **kwargs)
        self.fields['sender'].widget.attrs.update( {
            'placeholder': 'tcook@apple.com'
        })
        self.fields['sub'].widget.attrs.update( {
            'placeholder': 'hi'
        })
        self.fields['msg'].widget.attrs.update( {
            'placeholder': 'I love your work'
        })

class ImageUploadForm( BootstrapModelForm ):
    date = forms.DateField()
    # widget = forms.SelectDateWidget( empty_label = ( 'year', 'month', 'day' ), ) 

    class Meta():
        model = models.ImageUpload
        fields = '__all__'

    def __init__( self, *args, **kwargs ):
        '''
        This use of __init__ changes how Django renders forms which are called with template tags.
        '''
        super( ImageUploadForm, self ).__init__(*args, **kwargs)
        self.fields['frontpage'].widget.attrs.update( {
            'class': ''
        })
        self.fields['date'].widget.attrs.update( {
            'id': 'datepicker'
        })
