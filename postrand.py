#!/usr/bin/python

from os import walk
from os import rename
from os import path
from pynstagram import client
import random
import logging
import sys

caption_extras = " #hashtag"
username = "xxx"
password = "xxx"


file_dir = path.dirname(__file__)
origin = file_dir+"/to_post/"
posted_destination = file_dir+"/posted/"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=file_dir+'log.log',
                    filemode='a')

f = []
for (dirpath, dirnames, filenames) in walk(origin):
    f.extend(filenames)
if len(filenames) is 0:
    logging.warning('No more images to post')
    sys.exit()
image = random.choice(filenames)
image_path = origin+image


# Image caption comes from the filename
# my_image.jpg -> My Image
caption = image[0:image.find(".")].replace("_", " ").title()
caption = caption+caption_extras

pynstagram_client = client(username, password)
pynstagram_client.upload(image_path, caption)

# If image is not posted script will exit with exception
# no need to verify posting

logging.info("Posted: %s", image_path)

posted_image_path = posted_destination+image

try:
    rename(image_path, posted_image_path)
except OSError:
    pass

logging.info("Moved %s to: %s", image_path, posted_image_path)
