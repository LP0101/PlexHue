#!/usr/bin/python

from phue import Bridge
import os
import sys
import ast

b = Bridge('192.168.1.217')

if (sys.argv[1] == "Plex for LG (webOS 04.30.06)" or sys.argv[1] == 'LG 43UH6500-UB') and sys.argv[2] == 'agsl': 
    if os.path.isfile("room_s"):
        f = open("room_s", "r")
        room = ast.literal_eval(f.read())
        f.close()
        b.set_light([1, 2, 3], { 'bri': room['state']['bri'], 'on': True, 'transitiontime': 20, 'xy': room['state']['xy']})
        os.remove("room_s")
    else:
        b.set_light([1,2,3], {'bri': 254, 'on': True, 'transitiontime':20, 'xy': [0.3664, 0.3675]})
