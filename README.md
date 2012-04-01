pyLaunchpad
===========

Library to play with Novation Launchpad with Python
---------------------------------------------------
pyLaunchpad is the result of my experiments with using the Novation Launchpad as a scrolling display from python.
It uses pyPortmidi to talk to the device and pyGame for a simulator if you don't have have launchpads plugged in.

Ubuntu Linux
------------
You can install portMidi with:

    apt-get install python-pypm

Support for the Launchpad was added in Linux Kernel 2.6.37, so Linuxes with a newer kernel will not need any special drivers.

Mac OS X
--------
I have fond the easiest way is to install Macports and run:

    port install py27-game +portmidi

You will also need to install the Novation USB driver

License and Author
==================

The file images/text.png is based on the font minecraftia by Andrew Tyler
License: http://creativecommons.org/licenses/by-sa/3.0/us/

All other files:

Copyright 2011-2012 Robert (Jamie) Munro

Thanks to Matt Wescott for his help and inspiration.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
