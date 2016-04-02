#!/usr/bin/env python2

from __future__ import print_function
import qhue
import sys

CONFIG_FILE = "config"


"""
Print help on screen
"""
def print_help():
    pass



execfile(CONFIG_FILE)
print("Connecting...", end='')
b = qhue.Bridge(HUE_BRIDGE_IP, HUE_USERNAME)
print("ok")

#
# Scenes
#

# normal
print("Scene: normal...", end='')
b.scenes('normal', name="normal", lights=["4", "6"])
b.scenes['normal']['lightstates']['4'](on=True, hue=14000, effect="none", xy=[0.48, 0.41], bri=238, ct=400, sat=190)
b.scenes['normal']['lightstates']['6'](on=False)
print("ok")

# movie
print("Scene: movie...", end='')
b.scenes('movie', name="movie", lights=["4", "6"])
b.scenes['movie']['lightstates']['4'](on=True, hue=14000, effect="none", xy=[0.48, 0.41], bri= 40, ct=400, sat=190)
b.scenes['movie']['lightstates']['6'](on=False)
print("ok")

# morning
print("Scene: morning...", end='')
b.scenes('morning', name="morning", lights=["4", "5"])
b.scenes['morning']['lightstates']['4'](on=True, hue=10150, effect="none", xy=[0.57, 0.40], bri=254, ct=500, sat=252)
b.scenes['morning']['lightstates']['5'](on=True, hue= 1540, effect="none", xy=[0.65, 0.33], bri=  1, ct=500, sat=252)
print("ok")

# reading
print("Scene: reading...", end='')
b.scenes('reading', name="reading", lights=["4", "6"])
b.scenes['reading']['lightstates']['4'](on=False)
b.scenes['reading']['lightstates']['6'](on=True, bri=210)
print("ok")

# pre-bed
print("Scene: pre-bed...", end='')
b.scenes('pre-bed', name="pre-bed", lights=["4", "5", "6"])
b.scenes['pre-bed']['lightstates']['5'](on=True, hue=14000, effect="none", xy=[0.48, 0.41], bri= 40, ct=400, sat=190)
b.scenes['pre-bed']['lightstates']['4'](on=False)
b.scenes['pre-bed']['lightstates']['6'](on=False)
print("ok")

#
# Schedules
#
print("Schedule: wake up...", end='')
b.schedules['wake-up'](
    name="wake up",
    description="rise and shine, bitch!",
    command={
        'address': "/api/" + HUE_USERNAME + "/groups/0/action",
        'method': "PUT",
        'body': {
            'scene': "morning"
        }
    },
    status="enabled",
    localtime="W124/T05:30:00",
    http_method="PUT"
)
print("ok")

#
# Sensors
#

# Not sure if "1" was added by some other app or if it is programmed in by Philips

# Idaho Falls
lat  = "043.4665N"
long = "112.0341W"
b.sensors['1'](config={ 'lat' : lat, 'long' : long, 'sunriseoffset': 30, 'sunsetoffset' : -30 })


#
# Rules
#

# turn lights off after sunrise
b.rules(
    name="Lights off after sunrise",
    status="enabled",
    conditions=[
        { 'address': "/sensors/1/state/daylight", 'operator': "eq", 'value': "true" },
    ],
    actions=[
        { 'address': "/groups/0/action", 'method': "PUT", 'body': { 'on': False } }
    ],
    http_method="POST"
)

# turn scene "normal" on
b.rules(
    name="Lights on when sunset",
    status="enabled",
    conditions=[
        { 'address': "/sensors/1/state/daylight", 'operator': "eq", 'value': "false" },
    ],
    actions=[
        { 'address': "/groups/0/action", 'method': "PUT", 'body': { 'scene': "normal" } }
    ],
    http_method="POST"
)

