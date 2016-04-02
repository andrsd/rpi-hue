#!/usr/bin/env python2
"""
  Usage: ./light.py <light name> [ on | off ]
"""

import qhue
import sys

CONFIG_FILE = "config"


"""
Print help on screen
"""
def print_help():
	pass



execfile(CONFIG_FILE)
b = qhue.Bridge(HUE_BRIDGE_IP, HUE_USERNAME)

light_name_map = {}
lights = b.lights()
for l in lights:
	name = lights[l]['name'].upper()
	light_name_map[name] = l

ln = sys.argv[1].upper()
light_id = light_name_map[ln]

action = sys.argv[2]
if action == "on":
	b.lights[light_id].state(on=True)
elif action == "off":
	b.lights[light_id].state(on=False)
elif action == "" or action == "help":
	print_help()

