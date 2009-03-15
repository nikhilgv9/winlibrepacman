==================================
WinLibre Package Manager Proposal
==================================

**Contact**: *bertrand.cachet@gmail.com*

Scope
*****

Main Goal
=========

We want to develop a Windows package management system in order to ease the deployment of 
Open Source applications on Windows systems.

In deed there is no application of that sort onto Windows platform. Nowadays, users need to 
find application on the web, download/install/keep updated it by themselves. Moreover, there 
are a lot of different way to manage applications on Windows platform. End users need to know
all of them.

Package manager will be in charge of displaying informations about available packages to 
the user. User will be able to install/upgrade/remove the application he has selected. End 
user will manage his/her applications from a central place.

Our package manager will be able to handle dependencies which will ease the deployment of 
applications on Windows platforms because developers will not need to keep a watch to 
libraries they use anymore.

Description
===========

The mechanism is divided into several parts.

Packages
--------

To be able to install a software, it should be packaged. Package will be a simple 
compressed file (ZIP, TAR, XAR) which contains description of the software, specific
scripts (that will be used to install/remove/update/enumerate the application onto the 
OS). The binary representation of the application itself (list of binary files that need 
to be installed or an official/unofficial setup of the application) can be packed into the
package itself or would be downloaded from developer server.

Repository
----------

Place (WebServer, DVD) where we find informations about the software available in the 
distribution. There is two levels of informations: 
                                                              
* Generic: A list of the names, versions and descriptions of the applications which 
  will inform the user about which application is available.
* Specific: At a specific place, it is possible to find specific information on a given 
  application: URL of the package, dependencies, required ... which will be used to 
  install/remove/update the application itself.

Package Manager
---------------

Application used to search/install/remove/update applications on the user's Windows 
system. It will handle software dependencies will install libraries/applications needed 
by the software to run properly. User will interact with application using CLI or GUI.

Package Manager is divided in two parts:

* One will install/remove/update application using the package file.

+---------------------------------+-------------------------------------------------------+
| **wpkg** *action* <package>     | Install/remove/update software described into package |
|                                 | file. wpkg will use scripts located into the package  |
|                                 | and will use/download binary representation of the    |
|                                 | application                                           |
+---------------------------------+-------------------------------------------------------+
| **wpkg** *status* <package>     | Get stattus of the package.                           |
|                                 | Possible output:Installed/Not Installed/Update        |
|                                 | Available.                                            |
+---------------------------------+-------------------------------------------------------+
| **wpkg** *show* <package>       | Show information about package. It will output: name, |
|                                 | description, license and so on.                       |
+---------------------------------+-------------------------------------------------------+

* Another one will search/download packages from repository. It will also handle 
  dependencies.

+---------------------------------+-------------------------------------------------------+
| **wpckgmgr** *update*           | Updates package lists. Get last package list from     |
|                                 | repo                                                  |
+---------------------------------+-------------------------------------------------------+
| **wpckmgr** *action* <name>     | Install/update/remove package. Handles dependencies.  |
|                                 |                                                       |
+---------------------------------+-------------------------------------------------------+
| **wpckgmgr** *search* <keyword> | Search through name/description of packages. Outputs  |
|                                 | names of packages whose name or description fits the  |
|                                 | keyword                                               |
+---------------------------------+-------------------------------------------------------+
| **wpckgmgr** *show* <name>      | Outputs information about package. It outputs even if |
|                                 | package wasn't installed or downloaded. Manager gets  |
|                                 | information from package list.                        |
+---------------------------------+-------------------------------------------------------+

Package Creator
---------------
Used by developers to create package to deploy their application on Windows system.                                              


Technical requirement
*********************

The Repository Server
=====================

It's a RESTful web application where each URL represent a package:

* GET access is public and can return JSON, YAML or HTML formats. GET access 
  will be used by WinPacMan client to get information about the package.
* POST, UPDATE and DELETE access are protected (authentification via OpenID or 
  Google Account). These access are used by the Package Generator Tool 
  to update information about the package.

