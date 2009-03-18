#
# Copyright (c) 2004 Conectiva, Inc.
#
# Written by Gustavo Niemeyer <niemeyer@conectiva.com>
#
# This file is part of Smart Package Manager.
#
# Smart Package Manager is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# Smart Package Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Smart Package Manager; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
import os
import subprocess

if subprocess.mswindows:
    import msvcrt
    
    def funlock(fd):
        # On Windows system, we only need to close the file
        # to unlock it.
        pass
        
    def flock(fd, blocking=False, exclusive=False):
        pass
#        if blocking:
#            flags = msvcrt.LK_NBLCK
#        else:
#            flags = msvcrt.LK_LOCK
#        msvcrt.locking(fd.fileno(), flags, os.path.getsize(fd.name))
        
    def fopen(path, flags=os.O_RDONLY):
#        if os.path.isdir(path):
#            return open(os.path.join(path, 'lock'), 'w')
        return os.open(path, flags)
        
else:
    import fcntl
    
    def funlock(fd):
        fcntl.flock(fd, fcntl.F_UNLCK)
        
    def flock(fd, blocking=False, exclusive=False):
        if exclusive:
            flags = fcntl.LOCK_EX
        else:
            flags = fcntl.LOCK_SH
        if not blocking:
            flags |= fcntl.LOCK_NB
        fcntl.flock(fd, flags)
        
    def fopen(path, flags=os.O_RDONLY):
        fd = os.open(path, flags)
        flags = fcntl.fcntl(fd, fcntl.F_GETFD, 0)
        flags |= fcntl.FD_CLOEXEC
        fcntl.fcntl(fd, fcntl.F_SETFD, flags)
        return fd

class PathLocks(object):
    
    def __init__(self, force=True):
        self._lock = {}
        self._force = bool(force)

    def getForce(self):
        return self._force

    def setForce(self, flag):
        self._force = flag

    def __del__(self):
        # fcntl module may be destructed before we are.
        try:
            self.unlockAll()
        except TypeError, e:
            pass

    def unlockAll(self):
        # for path in self._lock:
        #     fd = self._lock[path]
        #     funlock(fd)
        #     os.close(fd)
        # self._lock.clear()
        pass

    def unlock(self, path):
        result = self._force
        # fd = self._lock.get(path)
        # if fd is not None:
        #     funlock(fd)
        #     os.close(fd)
        #     del self._lock[path]
        #     result = True
        return result
        
    
    def lock(self, path, exclusive=False, block=False):
        result = self._force
        # fd = self._lock.get(path)
        # if fd is None:
        #     fd = self._lock[path] = fopen(path, os.O_RDONLY)
        # try:
        #     flock(fd, block, exclusive)
        #     result = True
        # except IOError, e:
        #     pass
        return result
        
