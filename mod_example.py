import random
import urllib.request

def downloadImage(url):
    filename = str(random.randrange(1,1000))
    download = urllib.request.urlretrieve(url, filename)

downloadImage()

