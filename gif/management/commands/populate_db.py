import requests
from gif.models import Gif
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        load()
def load():

    print(':::LOADING DATASET:::')
    gifs_raw = requests.get("https://raw.githubusercontent.com/raingo/TGIF-Release/master/data/tgif-v1.0.tsv").text

    gifs_matrix=[]
    for line in gifs_raw.splitlines()[1:1000]:
        gifs_matrix.append(line.split("\t"))

    for gif in gifs_matrix:
        url = gif[0]
        desc = gif[1]

        Gif.objects.create(url=url, description=desc)
