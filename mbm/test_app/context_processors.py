from . import models

def uprofile_processor( request ):
    profile = models.UserProfile.objects.values()[0]
    return { 'profile': profile }
