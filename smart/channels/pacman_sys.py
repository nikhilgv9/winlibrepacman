from smart.backends.pacman.loader import PacManDBLoader
from smart.channel import PackageChannel
from smart import *
import os

class PacManSysChannel(PackageChannel):

    def __init__(self, *args):
        super(PacManSysChannel, self).__init__(*args)

def create(alias, data):
    return PacManSysChannel(    data["type"],
                                alias,
                                data["name"],
                                data["manual"],
                                data["removable"],
                                data["priority"]
                            )

# vim:ts=4:sw=4:et
