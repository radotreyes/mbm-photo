from django.contrib import admin
from test_app.models import AccessRecord, Topic, Webpage, UserProfile

# Register your models here.
admin.site.register( AccessRecord )
admin.site.register( Topic )
admin.site.register( Webpage )
admin.site.register( UserProfile )
