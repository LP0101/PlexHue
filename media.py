#!/usr/bin/python

from phue import Bridge
import os
import sys
import requests

b = Bridge('192.168.1.217')
r = (requests.get("http://192.168.1.217/api//sensors/"))
lightlevel = r.json()['18']['state']['lightlevel']

if (sys.argv[1] == "Plex for LG (webOS 04.30.06)" or sys.argv[1] == 'LG 43UH6500-UB') and sys.argv[2] == 'agsl': 
    if not os.path.isfile('room_s'):
        f = open("room_s", "w")
        print(b.get_light(2), file=f)
        f.close()
    if lightlevel < 10500:
        b.set_light(1, {'bri' : 80, 'xy' : [0.1538, 0.0722], 'transitiontime': 20})
        b.set_light([2,3], {'on': False, 'transitiontime': 20})
