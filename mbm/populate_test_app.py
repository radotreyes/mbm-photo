import os
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'mbm.settings' )

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from test_app import models
from faker import Faker

fakegen = Faker()
topics = [ 'Search', 'Social', 'Marketplace', 'News', 'Games' ]

# def add_topic():
#     t = Topic.objects.get_or_create( tpc_name = random.choice( topics ))[0]
#     t.save()
#     return t


models.ImageUpload.objects.all().delete()

# def get_image_uploads():
#     iu = models.ImageUpload.objects.all().values()[0]
#     print( type( iu ) )
#     # entries = [ entry for n in iu ]
#     # dates = models.ImageUpload.objects.values( 'date' )[0]
#     # print( entries )
#     # return entries
#
# get_image_uploads()
#
# def populate():
#
#     for entry in fields:
#         # get topic for entry
#         # tpc = add_topic()
#
#         # create fake data for that entry
#         fake_date = fakegen.date()
#
#         # fake_url = fakegen.url()
#         # fake_name = fakegen.company()
#         # fake_email = fakegen.email()
#         #
#         # # create webpage for entry
#         # webpg = Webpage.objects.get_or_create( topic = tpc, name = fake_name, url = fake_url )[0]
#         #
#         # # create fake access record
#         # arec = AccessRecord.objects.get_or_create( name = webpg, date = fake_date )[0]
#
# if __name__ == '__main__':
#     print( 'Populating...' )
#     populate( 20 )
#     print( 'Models populated.' )
