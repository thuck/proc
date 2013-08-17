from .basic import ProcFile
from collections import namedtuple


class Consoles(ProcFile):
    filename = '/proc/consoles'
    Console = namedtuple('Console', ['operations', 'flags', 'major', 'minor'])

    def names(self):
        return [line.split()[0] for line in self._readfile()]

    def get(self, name, default=None):
        for line in self._readfile():
            console_info = line.replace('(', '').replace(')', '').split()
            if name == console_info[0]:
                major, minor = console_info[-1].split(':')
                return [console_info[1],
                        ''.join(console_info[2:-1]), major, minor
                        ]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            return self.Console(*tuple(self.get(name)))

        else:
            raise AttributeError

if __name__ == '__main__':
    CONSOLES = Consoles()
    print(CONSOLES.names())
    print(CONSOLES.get('tty0'))
    print(CONSOLES.tty0.operations)
    print(CONSOLES.tty0.flags)
    print(CONSOLES.tty0.major)
    print(CONSOLES.tty0.minor)
