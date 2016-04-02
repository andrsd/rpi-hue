RPi-HUE
=======

Set of simple scripts to control Philips HUE lights.


Prerequisites
-------------

* [qhue](https://github.com/quentinsf/qhue)
* Philips bridge with API 1.11 or better


Usage
-----

First run `init.py` to setup a new user. This will produce `config` file, which is used by other scripts.

`setup.py` creates some scenes, sets up some niceties.

* `all-off.py` -- turn off all lights
* `light.py` -- control a single light
* `scene.py` -- turn on a scene


Why?
----

The Philips bride cam turn lights on/off based on sunset/sunrise, but this is not available via the iPhone
app, so people have to use IFTTT app.  Even more, one can setup an offset for the sunset and surise!

Simply said, the API offers a lot more than the apps can do, so why not to use it!


Thanks
------

* Dan Krause for [ssdp.py](https://gist.github.com/dankrause/6000248)


