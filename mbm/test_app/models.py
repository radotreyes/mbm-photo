from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Topic( models.Model ):
    tpc_name = models.CharField( max_length = 264, unique = True )

    def __str__( self ):
        return self.tpc_name

class Webpage( models.Model ):
    topic = models.ForeignKey( Topic )
    name = models.CharField( max_length = 264, unique = True )
    url = models.URLField( unique = True )

    def __str__( self ):
        return self.name

class AccessRecord( models.Model ):
    name = models.ForeignKey( Webpage )
    date = models.DateField()

    def __str__( self ):
        return str( self.date )

class ImageUpload( models.Model ):
    PORTRAIT = 'portrait'
    LANDSCAPE = 'landscape'
    CATEGORIES = (
        ( PORTRAIT, 'Portrait'),
        ( LANDSCAPE, 'Landscape' )
    )

    image = models.ImageField( upload_to = 'user_img/' )
    title = models.CharField( max_length = 50 )
    category = models.CharField( max_length = 20, choices = CATEGORIES,
        default = PORTRAIT )
    date = models.DateField( default = '0000-00-00', verbose_name = 'Date (YYYY-MM-DD)')
    camera = models.CharField( max_length = 20 )
    location = models.CharField( max_length = 100 )
    frontpage = models.BooleanField( default = False, verbose_name = 'Display on frontpage?' )

    def __str__( self ):
        return str( self.id )

class EmailRequest( models.Model ):
    sender = models.EmailField( verbose_name = 'Your e-mail')
    sub = models.CharField( max_length = 100, verbose_name = 'Subject' )
    msg = models.TextField( max_length = 1000, verbose_name = 'Message (be nice)' )

class UserProfile( models.Model ):
    ppic = models.ImageField( upload_to = 'ppic/', verbose_name = 'Profile picture' )
    city = models.CharField( max_length = 20 )
    state = models.CharField( max_length = 2 )
    fb = models.URLField( verbose_name = 'Facebook URL' )
    fb_handle = models.CharField( default = 'handle', max_length = 100, verbose_name = 'Facebook name' )
    ig = models.URLField( verbose_name = 'Instagram' )
    ig_handle = models.CharField( default = 'handle', max_length = 100, verbose_name = 'Instagram handle' )
    tw = models.URLField( verbose_name = 'Twitter' )
    tw_handle = models.CharField( default = 'handle', max_length = 100, verbose_name = 'Twitter handle' )
    desc = models.TextField( max_length = 3000, verbose_name = 'About me' )
    cv = models.URLField( default = 'http://google.com', verbose_name = 'Link to resume/CV' )

    def __str__( self ):
        return 'user profile'

@receiver( post_delete, sender = ImageUpload )
def mymodel_delete( sender, instance, **kwargs ):
    # Pass false so FileField doesn't save the model.
    instance.image.delete( False )
