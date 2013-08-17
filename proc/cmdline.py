from .basic import ProcFile


class CMDLine(ProcFile):
    filename = '/proc/CMDline'

    @property
    def value(self):
        return ' '.join(self._readfile())

    def parameters(self):
        return [field.split('=', 1)
                for line in self._readfile()
                for field in line.split(' ')
                ]

    def has_parameter(self, parameter):
        for param in self.parameters():
            if parameter == param[0]:
                return True

        else:
            return False

    def get(self, key, default=None):
        for param in self.parameters():
            if key == param[0] and len(param) > 1:
                return param[1]

        else:
            return default

if __name__ == '__main__':
    CMD = CMDLine()
    print(CMD.value)
    print(CMD.parameters())
    print(CMD.has_parameter('BOOT_IMAGE'))
    print(CMD.has_parameter('BOOT_IMAGEL'))
    print(CMD.get('BOOT_IMAGE'))
    print(CMD.get('BOOT_IMAGEL'))
