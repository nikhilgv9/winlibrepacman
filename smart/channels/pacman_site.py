from smart.channel import PackageChannel
from smart.backends.pacman.loader import PacManXMLLoader
from smart.const import SUCCEEDED, FAILED, NEVER
from smart.util.filetools import getFileDigest

class PacManSiteChannel(PackageChannel):
    """
    In charge of downloading informations from URL \
    and to create adapted Loader modules.
    
    Loader modules will parse data contained into \
    downloaded file to get informations about \
    available packages.
    """

    def __init__(self, baseurl, *args):
        super(PacManSiteChannel, self).__init__(*args)
        self._baseurl = baseurl
        self._digest = "digest"
        
    def fetch(self, fetcher, progress):
        fetcher.reset()
        info = {}#{'uncomp': True}
        item = fetcher.enqueue(self._baseurl, **info)        
        fetcher.run(progress=progress, what=True)
        if item.getStatus() == SUCCEEDED:
            localpath = item.getTargetPath()
            digest = getFileDigest(localpath)
            if digest == self._digest:
                return True
        
            self.removeLoaders()
            loader = PacManXMLLoader(localpath)
            loader.setChannel(self)
            self._loaders.append(loader)
        else:
            return False
        self._digest = digest
        return True
        
    def addLoaders(self, cache):
        for loader in self._loaders:
            cache.addLoader(loader)

def create(alias, data):
    return PacManSiteChannel(   data['baseurl'],
                                data["type"],
                                alias,
                                data["name"]
                                # data["name"],
                                # data["manual"],
                                # data["removable"],
                                # data["priority"]
                            )

# vim:ts=4:sw=4:et
