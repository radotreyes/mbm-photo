from django.contrib import admin
from . import models

# Register your models here.
admin.site.register( models.AccessRecord )
admin.site.register( models.Topic )
admin.site.register( models.Webpage )
admin.site.register( models.ImageUpload )
admin.site.register( models.UserProfile )
admin.site.register( models.EmailRequest )
