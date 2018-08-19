import requests
from gif.models import Gif
def load():

    print(':::LOADING DATASET:::')
    gifs_raw = requests.get("https://raw.githubusercontent.com/raingo/TGIF-Release/master/data/tgif-v1.0.tsv").text

    gifs_matrix=[]
    for line in gifs_raw.splitlines():
        gifs_matrix.append(line.split("\t"))

    for gif in gifs_matrix:
        url = gif[0]
        desc = gif[1]

        Gif.objects.create(url=url, description=desc)
