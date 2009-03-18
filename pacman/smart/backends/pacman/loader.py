import os

from pacman.smart.cache import Loader, PackageInfo
from base import PacManPackage, PacManProvides, PacManUpgrades
from elementtree import ElementTree


class PacManPackageInfo(PackageInfo):

    def __init__(self, package, info):
        super(PacManPackageInfo, self).__init__(package)
        self._info = info

    def getGroup(self):
        return "PacMan"

    def getSummary(self):
        return self._info.get("summary", "")

    def getDescription(self):
        return self._info.get("description", "")

    def getURLs(self):
        info = self._info
        if "packageurls" in info:
            return info['packageurls']
            urls = []
            for child in info['packageurls'].getchildren():
                urls.append(child.text)
            return urls
        return []

    def getPathList(self):
        return self._info.get("filelist", [])

class PacManLoader(Loader):
    """
    Module in charge of downloading information about 
    packages from a given URL
    """

    def __init__(self):
        Loader.__init__(self)
        
    def load(self):
        """
        Load packages returned by getInfoList
        """
        
        provargs = reqargs = upargs = cnargs = []
        
        for info in self.getInfoList():
            name = info['name']
            version = info['version']
            prvargs = [(PacManProvides, name, version)]
            upgargs = [(PacManUpgrades, name, "<", version)]
            pkg = self.buildPackage((PacManPackage, name, version), 
                                    provargs, 
                                    reqargs, 
                                    upargs, 
                                    cnargs)
            pkg.loaders[self] = info
            
    def getInfoList(self):
        return []
    
    def getInfo(self, pkg):
        return PacManPackageInfo(pkg, pkg.loaders[self])

class PacManXMLLoader(PacManLoader):
    def __init__(self, filename):
        super(PacManLoader, self).__init__()
        self._filename = filename
    
    def getInfoList(self):
        root = ElementTree.parse(self._filename).getroot()
        packages = []
        for package in root.find('packages').getchildren():
            info = {}
            for child in package.getchildren():
                if child.getchildren():
                    info[child.tag] = []
                    for subchild in child.getchildren():
                        info[child.tag].append(subchild.text)
                else:
                    info[child.tag] = child.text
            packages.append(info)
        return packages
        
    
    def getLoadSteps(self):
        root = ElementTree.parse(self._filename).getroot()
        return len(root.find('packages').getchildren())
        
# vim:ts=4:sw=4:et
