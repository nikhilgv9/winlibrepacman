from pacman.smart.const import INSTALL, REMOVE
from pacman.smart.pm import PackageManager
from pacman.smart import *
import commands

class PacManPackageManager(PackageManager):
    """
    This is the module in charge of performing actions
    required by user on selected packages.
    Actions can be: INSTALL, UPGRADE, REMOVE
    
    """

    def commit(self, changeset, pkgpaths):
        install = {}
        remove = {}
        for pkg in changeset:
            if changeset[pkg] is INSTALL:
                install[pkg] = True
            else:
                remove[pkg] = True
        upgrade = {}
        for pkg in install:
            for upg in pkg.upgrades:
                for prv in upg.providedby:
                    for prvpkg in prv.packages:
                        if prvpkg.installed:
                            if prvpkg in remove:
                                del remove[prvpkg]
                            if pkg in install:
                                del install[pkg]
                            upgrade[pkg] = True
                            
        for pkg in install:

#            status, output = commands.getstatusoutput("installpkg %s" % 
#                                                        pkgpaths[pkg][0])
            status, output = 0, 'Package installed'
            print pkg, output, status, pkg.installed

        for pkg in upgrade:

#            status, output = commands.getstatusoutput("upgradepkg %s" %
#                                                      pkgpaths[pkg][0])
            status, output = 0, 'Package upgraded'
            print pkg, output, status

        for pkg in remove:
#            status, output = commands.getstatusoutput("removepkg %s" %
#                                                      pkg.name)
            status, output = 0, 'Package removed'
            print pkg, output, status

# vim:ts=4:sw=4:et
