from smart.const import INSTALL, REMOVE
from smart.pm import PackageManager
from smart import *
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
            status, output = 0, 'installed'
            print 'Package %s is %s. Installed: %s' % (pkg, output, pkg.installed)

        for pkg in upgrade:

#            status, output = commands.getstatusoutput("upgradepkg %s" %
#                                                      pkgpaths[pkg][0])
            status, output = 0, 'upgraded'
            print 'Package %s is %s. Installed: %s' % (pkg, output, pkg.installed)

        for pkg in remove:
#            status, output = commands.getstatusoutput("removepkg %s" %
#                                                      pkg.name)
            status, output = 0, 'removed'
            print 'Package %s is %s. Installed: %s' % (pkg, output, pkg.installed)

# vim:ts=4:sw=4:et
