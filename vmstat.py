from basic import ProcFile
from collections import namedtuple

class VMStat(ProcFile):
    filename = '/proc/vmstat'

    def names(self):
        return [line.split()[0] for line in self._readfile()]

    def get(self, stat_name, default = None):
        for line in self._readfile():
            stat_info = line.split()
            if stat_name == stat_info[0]:
                return stat_info[1]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            return int(self.get(name))

        else:
            raise AttributeError

    


if __name__ == '__main__':
    vmstat = VMStat()
    print vmstat.pgscan_kswapd_normal
    print vmstat.nr_free_pages
    
