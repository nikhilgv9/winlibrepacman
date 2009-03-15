.. _server-specs:

Server Specifications
#####################

Introduction
============

The Package Manager Server is a Django Application hosted on App Engine.


Details
=======
  * [http://en.wikipedia.org/wiki/Representational_State_Transfer RESTful] interface
  * Formats supported : [http://www.json.org/ JSON], [http://www.yaml.org/ YAML], HTML
  * GET Access : Everyone
  * POST, UPDATE, DELETE : Need authentication
  * Authentication : OpenID / Google Account 
  * Will serve Packages and MetaPackages descriptions
  * Replication : synchronize with mirrors

Data Model
==========
Package
-------

+-----------------+----------------+
|        Name     |          Type  |
+=================+================+
|        Name     |         Char   |
+-----------------+----------------+
|       Version   |       Char     |
+-----------------+----------------+
|       Date      |        Date    |
+-----------------+----------------+
|       Is Meta   |        Boolean |
+-----------------+----------------+
|    Dependencies |       Table    |
+-----------------+----------------+
|       Tag       |      Table     |
+-----------------+----------------+
|      Ratings    |      Integer   |
+-----------------+----------------+
|    Description  |      Text      |
+-----------------+----------------+
|    ScreenShots  |     Images     |
+-----------------+----------------+
|      Logo       |    Image       |
+-----------------+----------------+
| Package file    |     URL        |
+-----------------+----------------+
|      Licence    |    Char        |
+-----------------+----------------+
|      Web        |      URL       |
+-----------------+----------------+
|      Sources    |      URL       |
+-----------------+----------------+
|      SHA1/MD5   |      Text      |
+-----------------+----------------+
|  Supported  OS  |   Table        |
+-----------------+----------------+


Distribution/ Profile
----------------------

+-----------------+----------------+
|        Name     |          Type  |
+=================+================+
|     Name        |      Char      |
+-----------------+----------------+
|   Packages      |    Table       |
+-----------------+----------------+
|    Categories   |                |
+-----------------+----------------+
|    MetaData     |                |
+-----------------+----------------+
|     Version     |       Char     |
+-----------------+----------------+
|     Date        |      Date      |
+-----------------+----------------+
|   Description   |      Text      |
+-----------------+----------------+

Package File Structure
======================
Archive:
	- Description File : Package Data Model in YAML
	- Python Scripts : Install, Uninstall, Enumeration, Update
	- Data-File Archive

The packages won't be hosted on the Package manager server but on each project's server.

Links
-----
	- Django: http://www.djangoproject.com/
	- App Engine: http://code.google.com/appengine/
	- Melange : http://code.google.com/p/soc/
	