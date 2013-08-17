from .basic import ProcFile


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
    LOADAVG = LoadAvg()
    print(LOADAVG.five)
    print(LOADAVG.ten)
    print(LOADAVG.fifteen)
    print(LOADAVG.runnable_entities)
    print(LOADAVG.existing_entities)
    print(LOADAVG.last_pid_created)
