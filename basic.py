
class ProcFile(object):

    @property
    def value(self):
        return ' '.join(self._readfile())

    def _readfile(self):
        with open(self.filename) as opened_file:
            return [line.strip() for line in opened_file.xreadlines() if '#' not in line]

