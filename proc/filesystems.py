from basic import ProcFile
from collections import namedtuple

class Filesystems(ProcFile):
    filename = '/proc/filesystems'
    Filesystem = namedtuple('Filesystem', ['used'])

    @property
    def value(self):
        return ' '.join(self._readfile())

    def names(self):
        fs_names = []
        for line in self._readfile():
            fs_info = line.split('\t')
            if len(fs_info) > 1:
                fs_names.append(fs_info[1])

            else:
                fs_names.append(fs_info[0])
            
        return fs_names

    def get(self, fs_name, default = None):
        for line in self._readfile():
            fs_info = line.split('\t')
            if len(fs_info) > 1 and fs_name == fs_info[1]:
                return False

            elif fs_name == fs_info[0]:
                return True

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():            
            return self.Filesystem(self.get(name))

        else:
            raise AttributeError


if __name__ == '__main__':
    filesystem = Filesystems()
    print filesystem.value
    print filesystem.names()
    print filesystem.ext4
    print filesystem.ext4.used
    print filesystem.sockfs
    print filesystem.sockfs.used
