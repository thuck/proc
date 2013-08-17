from itertools import groupby

class ProcFile(object):

    @property
    def value(self):
        return ' '.join(self._readfile())

    def _readfile(self):
        with open(self.filename) as opened_file:
            return [line.strip() for line in opened_file if line.strip() and '#' not in line[0]]

    def _readfile_inblocks(self):
        with open(self.filename) as opened_file:
           tmp = [tuple(group) for key,group in itertools.groupby(opened_file, lambda line: line == '\n')]

        return [line for line in tmp if len(line) > 1]

    def _writefile(self, line):
        with open(self.filename, 'w+') as opened_file:
            opened_file.write(line)
            
