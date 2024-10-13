import requests 
import json
import random
token = "MLY|7884436731651628|991d31489dc0ba2a68fd9c321c4d2cd1"
latlong = ""

base = "https://graph.mapillary.com/images?access_token=MLY|7884436731651628|991d31489dc0ba2a68fd9c321c4d2cd1&fields=id&bbox=" 
min_long = random.randint(-180, 175)
min_lat = random.randint(-90, 85)
max_long = min_long + 5
max_lat = min_lat + 5
bbox = str(min_long) + "," + str(min_lat) + "," + str(max_long) + "," + str(max_lat)
bbox1 = "-180,-90,180,90"
print(bbox1)
x = requests.get(base + bbox1)
parsed_data = json.loads(x.text)
print(parsed_data)
print(base + bbox1)
print(x.text)

## check format in image you
## you need a bounding box to define the area it takes images over

## you can get images a bunch of images and you need to extract them
## 4 d.p. roughly on coordinates to get a shortlist of images
 