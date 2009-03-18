==================================================================
Tutorial to start working on the WinLibre Package Manager project
==================================================================

Development Environment
***********************

Source Code
===========

The repository of the source code is now on `github <http://github.com/bcachet/winlibrepacman>`_ 
so, to get WinLibre source code, you will need to install git version control system. You can 
download binaries for your OS from `here <http://git-scm.com/download>`_ and find information 
on how to use git with github `here <http://github.com/guides/home>`_.


Prepare Development Environment
===============================

First you will need to generate the virtual environnement which will contain all the python libraries 
we need for our development.
To do this, launch the following command from the project directory:
  python bootstrap.py

In our application, we download some file from the repository server. Actually this repository server 
does not exist on the Web. At this time our "repository" is a local HTTP server. You will need to 
specify the address of your local HTTP server in winlibre.py file.

You can use EasyPHP to manage a HTTP server very easily on Windows.

Structure of the project
========================

Here is the structure of the source code when you download it:

+-------------+--------------------+------------------------------------------------------------+
|   Type      |  File Name         |                        Description                         |
+=============+====================+============================================================+
|   file      | bootstrap.py       | Script that generates the virtual environnement used for   |
|             |                    | our development.                                           |
|   file      | winlibre.py        | Application launcher.                                      |
|             |                    |                                                            |
+-------------+--------------------+------------------------------------------------------------+
|  directory  | docs/              | *source* directory contains all the documents that will be |
|             |   docs/source      | used to generate the documentation.                        |
|             |                    |                                                            |
|             |   docs/build       | *build* directory contains the generated documentation     |
+-------------+--------------------+------------------------------------------------------------+
|  directory  | pacman/            | *smart* directory contains the source code of the SMART    |
|             |   pacman/smart     | library.                                                   |
|             |                    |                                                            |
|             |                    | *client* directory contains the source code of the client  |
|             |   pacman/client    | application.                                               |
|             |                    |                                                            |
|             |                    | *server* directory contains the source code of the         |
|             |   pacman/server    | repository server.                                         |
+-------------+--------------------+------------------------------------------------------------+
|  directory  | pacmandir/         | *pacmandir* directory is the working directory of the      |
|             |                    | SMART library. Cached data will be stored here.            |
|             |   pacmandir/config |                                                            |
+-------------+--------------------+------------------------------------------------------------+
|   file      | pavement.py        | Paver configuration file.                                  |
+-------------+--------------------+------------------------------------------------------------+
|   file      | setup.py           | Alias to the Paver utility to be compatible with distutils |
+-------------+--------------------+------------------------------------------------------------+

Paver scripting tool
====================

We manage our project using the `Paver <http://www.blueskyonmars.com/projects/paver/>`_ scripting 
tool. We use it to generate the documentation (using the `Sphinx <http://sphinx.pocoo.org/>`_ 
tool), find and launch unittests (via the `nose <http://somethingaboutorange.com/mrl/projects/nose/>`_ 
tool).

You can perform several actions:

  * Generating documentation: 
    ./bin/paver html 

  * Finding and performing unittests:
    ./bin/paver test

  * Cleaning *.pyc and temporary files:
    ./bin/paver clean

  * Cleaning generating documentation:
    ./bin/paver doc_clean

Used Libraries
**************

SMART
=====

Our development is axis around SMART library. We use it to get the list of available packages, 
to download them, and to handle cached files. 

The *pacman/smart* directory contains the SMART source code that we have modified to make it run onto 
windows platform. 

Every basic commands are handle from the *commands* which call the *controller* module (from control.py) to 
perform them. 

Controller module get list of available packages by fetching channels. All supported channels (such as apt, rpm, yast) defined some specific files into the *channels* directory. From these files SMART knows how to 
get informations from available packages from repositories.

SMART interact with packages using backends adapted to the channel that has been used to get these packages. All the supported channels define some backends in the *backends* directory. These backends will be used 
to get informations about packages.

We will study an example, installing firefox on Ubuntu using apt channel from SMART: 

  * Controller gets information about available packages using the code into *channels/apt_deb** files. SMART will search for firefox package. As soon as it find it, it will get informations about it using the *backends/deb/** files. 
  * From these informations it will find dependencies. From *backends/deb/** files it will know how to call *apt* tool to install dependencies and firefox packages.

SMART has its own CLI/GUI. We can use them to test our Windows backend and then develop our own 
solution.


