#!/usr/bin/env python2
"""
  Turn a scene on

  Usage: ./scene.py <scene name>
"""

import qhue
import sys


CONFIG_FILE = "config"

execfile(CONFIG_FILE)
b = qhue.Bridge(HUE_BRIDGE_IP, HUE_USERNAME)
b.groups['0'].action(scene=sys.argv[1])

