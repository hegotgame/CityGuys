#! usr/bin/env python

from sys import argv
from os.path import exists
import simplejson as json 

script, in_file, out_file = argv

newdata = [];

data = json.load(open("x8rh-2ghp.json"))

for d in data:
    try:
        if(d['location_1']):
            newdata.append(d)
    except KeyError:
        continue


data = json.load(open("t2gy-r4x8.json"))

for d in data:
    try:
        if(d['location_1']):
            newdata.append(d)
    except KeyError:
        continue

data = json.load(open("soda-nax7-sy3a.json"))

for d in data:
    try:
        if(d['location_1']):
            newdata.append(d)
    except KeyError:
        continue

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d['location_1']["coordinates"][0], d["location_1"]["coordinates"][1]],
            },
        "properties" : d,
     } for d in newdata]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print geojson