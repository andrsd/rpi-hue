#!/bin/env python2

from __future__ import print_function
import ssdp
import qhue
import sys
import urlparse

def get_ip_address(location):
	parts = urlparse.urlparse(location)
	return parts.netloc.split(":")[0]

if len(sys.argv) == 1:
	print("Looking for bridges... ", end='')
	services = ssdp.discover("")
	hue_bridges = []
	for s in services:
		if s.hue_bridgeid != None:
			hue_bridges.append(s)
	print("done")

	if len(hue_bridges) == 1:
		hue_ip = get_ip_address(hue_bridges[0].location)
	else:
		print("Multiple bridges found:")
		for h in hue_bridges:
			print("  " + get_ip_address(h.location))
		print("")
		print("Run this script with the IP address you want to use")
		exit(0)
else:
	hue_ip = sys.argv[1]

print("Initializing... ", end='')
try:
	username = qhue.create_new_username(hue_ip)
except qhue.QhueException as err:
	print("\nError occurred while creating a new username: {}".format(err))
	exit(1)
print("done")

print("Writing config file... ", end='')
# create config
with open("config", "w") as cfg_file:
	cfg_file.write("HUE_BRIDGE_IP = \"" + hue_ip + "\"\n")
	cfg_file.write("HUE_USERNAME = \"" + username + "\"\n")
print("done")

