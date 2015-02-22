"""Filesystem and online API interactions to grab images"""

import os
import urllib, urlparse
import json

def download_images(name, n = 20, minx=-77.037564, miny=38.896662, maxx=-77.035564, maxy=38.898662):
    """This Panoramio image download code adapted from Jan Erik Solem
    Stores the images to folder img/{name}
    Arguments are longitudes (x) and latitudes (y), default is white house.
    Returns list of filenames
    """

    # query for images
    url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&'
    args = 'from=0&to=%d&minx=%f&miny=%f&maxx=%f&maxy=%f&size=medium' % (n, minx, miny, maxx, maxy)
    c = urllib.urlopen(url + args)

    # get the urls of individual images from JSON
    j = json.loads(c.read())
    imurls = []
    for im in j['photos']:
        imurls.append(im['photo_file_url'])

    if imurls:
        # ensure directory exists
        dir = "img/" + name + "/"
        d = os.path.dirname(dir)
        if not os.path.exists(d):
            os.makedirs(d)

        # download images
        print("fetching", len(imurls), "images")
        for url in imurls:
            image = urllib.URLopener()
            path = dir + os.path.basename(urlparse.urlparse(url).path.encode('utf8'))
            try:
                if not os.path.isfile(path):
                    image.retrieve(url, path)
            except:
                print("failed to retrieve " + path)

        print("done fetching", len(imurls), "images")

        return [dir + file for file in os.listdir(dir)]
    else:
        print("no images found")
        return []

def get_images(name):
    """Returns list of filenames"""
    dir = "img/" + name + "/"
    return [dir + file for file in os.listdir(dir)]

if __name__ == "__main__":
    # download_images('washington', 50, minx=-77.037564, miny=38.896662, maxx=-77.035564, maxy=38.898662)
    print(download_images('campanile', 50, -122.260434, 37.871816, -122.258434, 37.873816))