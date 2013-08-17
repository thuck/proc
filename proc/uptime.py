from .basic import ProcFile

class Uptime(ProcFile):
    filename = '/proc/uptime'

    @property
    def total(self):
        return float(self._readfile()[0].split()[0])

    @property
    def idle(self):
        return float(self._readfile()[0].split()[1])

if __name__ == '__main__':
    uptime = Uptime()
    print(uptime.total)
    print(uptime.idle)
