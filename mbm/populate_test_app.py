import os
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'mbm.settings' )

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from test_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = [ 'Search', 'Social', 'Marketplace', 'News', 'Games' ]

def add_topic():
    t = Topic.objects.get_or_create( tpc_name = random.choice( topics ))[0]
    t.save()
    return t

def populate( n = 5 ):
    for entry in range( n ):
        # get topic for entry
        tpc = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_email = fakegen.email()

        # create webpage for entry
        webpg = Webpage.objects.get_or_create( topic = tpc, name = fake_name, url = fake_url )[0]

        # create fake access record
        arec = AccessRecord.objects.get_or_create( name = webpg, date = fake_date )[0]

if __name__ == '__main__':
    print( 'Populating...' )
    populate( 20 )
    print( 'Models populated.' )
