#!/usr/bin/env python2
#
# Turn all lights off
#

import qhue

CONFIG_FILE = "config"

execfile(CONFIG_FILE)
b = qhue.Bridge(HUE_BRIDGE_IP, HUE_USERNAME)
b.groups['0'].action(on=False)

