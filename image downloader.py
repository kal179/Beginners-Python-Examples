import random
import urllib.request

get = str(input("Enter url of image to download :  "))

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

print(download_image(get))
