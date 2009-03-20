from pm import PacManPackageManager
from pacmanver import checkdep, vercmp, vercmpparts, splitrelease
from smart.cache import Package, globdistance, Provides, Depends, Upgrades

__all__ = ["PacManPackage", "PacManProvides", "PacManUpgrades"]

class PacManPackage(Package):

    packagemanager = PacManPackageManager
    __slots__ = ()

    def __init__(self, name, version):
        Package.__init__(self, name, version)

    def coexists(self, other):
        return not isinstance(other, PacManPackage)

    def matches(self, relation, version):
        return (not relation) or checkdep(self.version, relation, version)

    def search(self, searcher):
        myname = self.name
        myversion = self.version
        ratio = 0
        icase = searcher.ignorecase
        for nameversion, cutoff in searcher.nameversion:
            _, ratio1 = globdistance(nameversion, self.name, cutoff, icase)
            _, ratio2 = globdistance(nameversion,
                                     "%s-%s" % (self.name, myversion), 
                                     cutoff, 
                                     icase)
            _, ratio3 = globdistance(nameversion, "%s-%s" %
                                     (self.name, splitrelease(myversion)[0]),
                                     cutoff, 
                                     icase)
            ratio = max(ratio, ratio1, ratio2, ratio3)
        if ratio:
            searcher.addResult(self, ratio)

    def __lt__(self, other):
        rc = cmp(self.name, other.name)
        if type(other) is PacManPackage:
            if rc == 0 and self.version != other.version:
                rc = vercmp(self.version, other.version)
        return rc == -1

class PacManProvides(Provides):
    def __init__(self, name, version):
        Provides.__init__(self, name, version)

class PacManDepends(Depends):
    def __init__(self, name, relation, version):
        Depends.__init__(self, name, relation, version)

class PacManUpgrades(Upgrades):
    def __init__(self, name, relation, version):
        Upgrades.__init__(self, name, relation, version)

# vim:ts=4:sw=4:et
