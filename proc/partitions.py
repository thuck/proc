from .basic import ProcFile
from collections import namedtuple


class Partitions(ProcFile):
    filename = '/proc/partitions'
    Partition = namedtuple('Partitions', ['major', 'minor', 'blocks'])

    def names(self):
        return [line.split()[3].lower() for line in self._readfile()[1:]]

    def get(self, p_name, default=None):
        for line in self._readfile():
            p_info = line.split()
            if p_name == p_info[3]:
                return p_info[:3]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            major, minor, blocks = tuple(map(int, self.get(name)[:3]))
            return self.Partition(major, minor, blocks)

        else:
            raise AttributeError


if __name__ == '__main__':
    PARTITIONS = Partitions()
    print(PARTITIONS.names())
    print(PARTITIONS.get('sda1'))
    print(PARTITIONS.sda1.major)
    print(PARTITIONS.sda1.minor)
    print(PARTITIONS.sda1.blocks)
    print(PARTITIONS.sda6.blocks)
