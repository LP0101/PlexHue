#!/usr/bin/python

from phue import Bridge
import os
import sys
import ast

b = Bridge('<BRIDGE IP>')

if sys.argv[1] == "<CLIENT>" and sys.argv[2] == '<USER>':
    if os.path.isfile("room_s"):
        f = open("room_s", "r")
        room = ast.literal_eval(f.read())
        f.close()
        b.set_light([<ALL LIGHTS>], { 'bri': room['state']['bri'], 'on': True, 'transitiontime': 20, 'xy': room['state']['xy']})
        os.remove("room_s")
    else:
        b.set_light([<ALL LIGHTS>], {'bri': 254, 'on': True, 'transitiontime':20, 'xy': [0.3664, 0.3675]})
