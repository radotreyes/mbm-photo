from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
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
    frontpage = models.BooleanField( default = False, verbose_name = 'Display on frontpage?' )

    def __str__( self ):
        return str( self.id )

@receiver( post_delete, sender = ImageUpload )
def mymodel_delete( sender, instance, **kwargs ):
    # Pass false so FileField doesn't save the model.
    instance.image.delete( False )

# class ImageUploadAdmin(admin.ModelAdmin):
#     # Add it to the list view:
#     list_display = ( 'title', 'id', )
#     # Add it to the details view:
#     read_only_fields = ( 'id', )
#     #
#     # def image_id(self, obj):
#     #     return mark_safe('<a href="{}">{}</a>'.format(
#     #         reverse("admin:auth_user_change", args=(obj.user.pk,)),
#     #         obj.user.email
#     #     ))
#     # user_link.short_description = 'user'
