from basic import ProcFile

class CMDLine(ProcFile):
    filename = '/proc/cmdline'

    @property
    def value(self):
        return ' '.join(self._readfile())

    def parameters(self):
        return [field.split('=', 1) for line in self._readfile()
            for field in line.split(' ')]

    def has_parameter(self, parameter):
        for param in self.parameters():
            if parameter == param[0]:
                return True

        else:
                return False

    def get(self, key, default = None):
        for param in self.parameters():
            if key == param[0] and len(param) > 1:
                return param[1]

        else:
               return default
                

if __name__ == '__main__':
    a = CMDLine()
    print a.value
    print a.parameters()
    print a.has_parameter('BOOT_IMAGE')
    print a.has_parameter('BOOT_IMAGEL')
    print a.get('BOOT_IMAGE')
    print a.get('BOOT_IMAGEL')
    
