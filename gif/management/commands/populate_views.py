import requests
from gif.models import Gif
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        populate()

def populate():

    print(':::RECREATING VIEWS:::')
    queryset = Gif.objects.all()
    map(mapper,queryset)

def mapper(item):
    item.views = random.randint(0,1000)
    item.save()
