.. _client-specs:

Client Specifications
#####################

Introduction
============

The Package Manger Client is a two layer software.
	- A windows service presenting a telnet interface
	- A GUI application with a Synaptic like interface

Moreover a Remote Adminitration GUI will allow to manage multiple computers in a Network

Details
=======

Windows Service
---------------
	- Python Based
	- Based on SMART, Python Package Manager
	- Provide a telnet interface
	- Connect to the Package Manager Server or to a local file repository (CD,...)

Features
^^^^^^^^
	- Install
	- Enumerate
	- Upgrade
	- Uninstall

Ideas @ GSoC Mentor Summit 08
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
.. image:: ./pics/IMG_0331.JPG

GUI
---

	- Communicate with the service through the telnet interface
	- Synaptic like GUI
	- Toolkit ?? Native, Qt, Gtk, WxPython, HTML + Gecko

Remote Adminitration
--------------------
	Could be integrated in the GUI application
	Allow to remotely install / upgrade / uninstall sotfware

Links
=====
	SMART : http://labix.org/smart
