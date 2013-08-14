from basic import ProcFile
from collections import namedtuple

class SlabInfo(ProcFile):
    filename = '/proc/slabinfo'
    Slab = namedtuple('Slab', ['active_objs', 'num_objs', 
                               'objsize', 'objperslab', 'pagesperslab',
                               'tunables', 'slabdata'])
    Tunables = namedtuple('Tunables', ['limit', 'batchcount', 'sharedfactor'])
    SlabData = namedtuple('SlabData', ['active_slabs', 'num_slabs', 'sharedavail'])

    def names(self):
        return [line.split()[0].lower() for line in self._readfile()[1:]]

    def get(self, name, default = None):
        for line in self._readfile()[1:]:
            slab_info = line.split()
            if name == slab_info[0]:
                return slab_info[1:]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            slab_info = self.get(name)
            tunables = self.Tunables(int(slab_info[7]), int(slab_info[8]), int(slab_info[9]))
            slabdata = self.SlabData(int(slab_info[12]), int(slab_info[13]), int(slab_info[14]))

            return self.Slab(int(slab_info[0]), int(slab_info[1]), int(slab_info[2]),
                      int(slab_info[3]), int(slab_info[4]), tunables, slabdata)
            

        else:
            raise AttributeError

if __name__ == '__main__':
    slabinfo = SlabInfo()
#    print slabinfo.names()
    print slabinfo.get('nfsd4_lockowners')
    print slabinfo.nfsd4_lockowners

