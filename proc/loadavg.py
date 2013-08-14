from basic import ProcFile
from collections import namedtuple

class LoadAvg(ProcFile):
    filename = '/proc/loadavg'

    @property
    def five(self):
        return float(self._readfile()[0].split()[0])

    @property
    def ten(self):
        return float(self._readfile()[0].split()[1])

    @property
    def fifteen(self):
        return float(self._readfile()[0].split()[2])

    @property
    def runnable_entities(self):
        return int(self._readfile()[0].split()[3].split('/')[0])

    @property
    def existing_entities(self):
        return int(self._readfile()[0].split()[3].split('/')[1])

    @property
    def last_pid_created(self):
        return float(self._readfile()[0].split()[4])

if __name__ == '__main__':
    loadavg = LoadAvg()
    print loadavg.five
    print loadavg.ten
    print loadavg.fifteen
    print loadavg.runnable_entities
    print loadavg.existing_entities
    print loadavg.last_pid_created
    
