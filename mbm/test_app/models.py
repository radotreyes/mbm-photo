from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField( max_length = 50 )
    image = models.ImageField( upload_to = 'user_img/', blank = True )

    def __str__( self ):
        return str( self.id )
