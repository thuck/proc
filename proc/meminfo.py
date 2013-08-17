from .basic import ProcFile
from collections import namedtuple

class MemInfo(ProcFile):
    filename = '/proc/meminfo'

    def names(self):
        return [line.split(':')[0].lower() for line in self._readfile()]

    def get(self, name, default = None):
        for line in self._readfile():
            mem_info = line.split()
            if name + ':' == mem_info[0].lower():
                return int(mem_info[1])

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            return self.get(name)

        else:
            raise AttributeError


if __name__ == '__main__':
    meminfo = MemInfo()
    print(meminfo.memtotal)
    print(meminfo.memfree)
