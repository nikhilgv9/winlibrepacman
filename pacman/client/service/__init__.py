#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Bertrand Cachet on 2008-11-24.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt
import os

import smart
from smart.const import NEVER, ALWAYS

from smart.channels import pacman_site
from smart.commands import search, install, update

from client.service.const import DATADIR, PACMANDIR

if os.name == 'posix':
    from user import home
#    baseurl = 'file://' + os.path.join(home, 'Workspace/WinLibre/winlibrepacman/','test.xml')
    baseurl = "http://127.0.0.1/~bertrand/packages.xml"
if os.name == 'nt':
    baseurl = "http://127.0.0.1/winlibrepacman/packages.xml"
path = os.path.join(os.path.dirname(__file__), '../../..', 'packages.xml')
baseurl = 'file://%s' % path
print baseurl


class SmartCtrlr:
    def __init__(self):
        datadir = DATADIR
        config = os.path.join(PACMANDIR, 'config')
        self.ctrl = smart.init(datadir=DATADIR, configfile=config)
        data = {'baseurl': baseurl,
                'type':"pacman",
                'name':'pacman'
                }
        self._channels['pacman'] = pacman_site.create('pacman', data)
        
    def __getattr__(self, attr):
        return getattr(self.ctrl, attr)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

help_message = '''
The help message goes here.
'''

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value

        smart_ctrl = SmartCtrlr()
#        smart_ctrl.reloadChannels(caching=NEVER)

        smart.sysconf.set("remove-packages", False)
        opts = update.parse_options([])
        update.main(smart_ctrl, opts)
        opts = install.parse_options(['Package2'])
        install.main(smart_ctrl, opts)
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
#    except smart.Error, err:
#        print err


if __name__ == "__main__":
    sys.exit(main())
