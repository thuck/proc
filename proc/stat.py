from .basic import ProcFile
from collections import namedtuple

class Stat(ProcFile):
    filename = '/proc/stat'
    CpuStat = namedtuple('CpuStat', ['user', 'nice', 'sys', 'idle']) # Expand this to get more specific information based on the arc

    def names(self):
        return [line.split()[0] for line in self._readfile()]

    def get(self, name, default = None):
        for line in self._readfile():
            stat_info = line.split()
            if name == stat_info[0]:
                return stat_info[1:]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            if 'cpu' in name:
                user, nice, sys, idle = tuple(self.get(name)[:4])
                return self.CpuStat(int(user), int(nice), int(sys), int(idle))

            else:
                return int(self.get(name)[0])

        else:
            raise AttributeError


if __name__ == '__main__':
    stat = Stat()
    print(stat.names())
    print(stat.get('cpu'))
    print(stat.get('cpu0'))
    print(stat.get('ctxt'))
    print(stat.cpu)
    print(stat.cpu.user)
    print(stat.cpu.nice)
    print(stat.cpu.sys)
    print(stat.cpu.idle)
    print(stat.processes)
    print(stat.processes)
    print(stat.procs_running)
