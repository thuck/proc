from .basic import ProcFile
from collections import namedtuple


class CGroups(ProcFile):
    filename = '/proc/cgroups'
    CGroup = namedtuple('CGroup', ['hierarchy', 'num_cgroups', 'enabled'])

    @property
    def value(self):
        return ' '.join(self._readfile())

    def names(self):
        return [cg_info.split('\t')[0] for cg_info in self._readfile()]

    def get(self, cg_name, default=None):
        for line in self._readfile():
            line = line.split('\t')
            if cg_name == line[0]:
                return line[1:]

        else:
            return default

    def __getattr__(self, cg_name):
        if cg_name in self.names():
            hierarchy, num_cgroups, enabled = tuple(self.get(cg_name))
            return self.CGroup(int(hierarchy), int(num_cgroups), bool(enabled))

        else:
            raise AttributeError


if __name__ == '__main__':
    CGROUPS = CGroups()
    print(CGROUPS.cpuset)
    print(CGROUPS.cpuset.hierarchy)
    print(CGROUPS.cpuset.num_cgroups)
    print(CGROUPS.cpuset.enabled)
    print(CGROUPS.perf_event)
