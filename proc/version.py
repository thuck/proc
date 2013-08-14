from basic import ProcFile
from collections import namedtuple

class Version(ProcFile):
    filename = '/proc/version'

    @property
    def ostype(self):
        return self._readfile()[0].split()[0]

    @property
    def osrelease(self):
        return self._readfile()[0].split()[2]

    @property
    def osversion(self):
        return '#%s' % self._readfile()[0].split('#')[-1]

if __name__ == '__main__':
    version = Version()
    print version.value
    print version.ostype
    print version.osrelease
    print version.osversion
