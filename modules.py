from basic import ProcFile
from collections import namedtuple

class Modules(ProcFile):
    filename = '/proc/modules'
    Module = namedtuple('ModuleInfo', ['memory_size',
                            'instances_counter', 'dependency',
                            'state', 'memory_offset'])

    @property
    def value(self):
        return ' '.join(self._readfile())

    def names(self):
        return [line.split(' ')[0] for line in self._readfile()]

    def get(self, module_name, default = None):
        for line in self._readfile():
            line = line.split(' ')
            if line[0] == module_name:
                return line[1:]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            (memory_size,instances_counter,
            dependency, state, memory_offset) = tuple(self.get(name))
            return self.Module(int(memory_size), int(instances_counter),
                                dependency, state, memory_offset)

        else:
            raise AttributeError 


if __name__ == '__main__':
    modules = Modules()
    #print modules.value
    print modules.names()
    print modules.get('i915')
    print modules.get('i915a')
    print modules.i915.memory_offset
    print modules.i915.instances_counter
    print modules.i915.dependency
    print modules.i915.state
    print modules.i915.memory_size
