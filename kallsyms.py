from basic import ProcFile
from collections import namedtuple

class KAllSyms(ProcFile):
    filename = '/proc/kallsyms'
    KSym = namedtuple('KSym', ['address', 'type', 'module'])

    def names(self):
        return [field.split()[2].lower() for field in self._readfile()]

    def get(self, ksym_name, default = None):
        for line in self._readfile():
            ksym_info = line.split()
            if ksym_name == ksym_info[2].lower():
                module = ksym_info[3] if len(ksym_info) > 3 else None
                return [ksym_info[0], ksym_info[1], module]

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            return self.KSym(*tuple(self.get(name)))

        else:
            raise AttributeError

if __name__ == '__main__':
    kallsyms = KAllSyms()
#    print kallsyms.names()
    print kallsyms.get('show_bnumendpoints')
    print kallsyms.show_bnumendpoints.address
    print kallsyms.show_bnumendpoints.type
    print kallsyms.show_bnumendpoints.module
    
