import requests 
import json
import random
token = "MLY|7884436731651628|991d31489dc0ba2a68fd9c321c4d2cd1"
latlong = ""

 
min_long = round(random.uniform(-180, 179.98), 2)
min_lat = round(random.uniform(-90, 89.98), 2)
max_long = min_long + 0.02
max_lat = min_lat + 0.02
bbox = str(min_long) + "," + str(min_lat) + "," + str(max_long) + "," + str(max_lat)
print(bbox)

## check format in image you
## you need a bounding box to define the area it takes images over

## you can get images a bunch of images and you need to extract them
## 4 d.p. roughly on coordinates to get a shortlist of images
 