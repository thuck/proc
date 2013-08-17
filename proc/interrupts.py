from basic import ProcFile
from collections import namedtuple

class Interrupt(object):
    pass

class Interrupts(ProcFile):
    filename = '/proc/interrupts'

    def names(self):
        return [field.lower() for field in self._readfile()[0].split()]

    def get(self, cpu_name, default = None):
        info = self._readfile()
        try:
            header = info.pop(0).split()
            field = header.index(cpu_name.upper()) + 1
            #Some lines doesn't have all fields, so ignoring it
            #in the future it should be taken in account
            return [line.split()[field] for line in info if len(line.split()) > 2]

        except ValueError:
            return default

    def __getattr__(self, name):
        if name in self.names():
            interrupt = Interrupt()
            var_names = []
            info = self._readfile()
            info.pop(0)
            for line in info:
                fields = line.split()
                if fields[0].replace(':','').isdigit():
                    var_names.append(fields[-1].replace(':','').lower())

                else:
                    var_names.append(fields[0].replace(':','').lower())

            for key, value in zip(var_names, tuple(map(int, self.get(name)))):
                setattr(interrupt, key, value)

            return interrupt

        else:
            raise AttributeError


if __name__ == '__main__':
    interrupts = Interrupts()
    print interrupts.names()
    print interrupts.get('cpu1')
    print interrupts.cpu1.timer
