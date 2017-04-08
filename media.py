#!/usr/bin/python

from phue import Bridge
import os
import sys

b = Bridge('<BRIDGE IP>')

if sys.argv[1] == "<CLIENT>" and sys.argv[2] == '<USER>': 
    if not os.path.isfile('room_s'):
        f = open("room_s", "w")
        print(b.get_light(2), file=f)
        f.close()
    b.set_light(<AMBIENT LIGHT ID>, {'bri' : 80, 'xy' : [0.1538, 0.0722], 'transitiontime': 20})
    b.set_light([<OTHER LIGHTS>], {'on': False, 'transitiontime': 20})
