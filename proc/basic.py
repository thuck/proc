from itertools import groupby


class ProcFile(object):
    """Basic class that represent a proc file"""
    filename = ''

    @property
    def value(self):
        """Return the content of the file """
        return ' '.join(self._readfile())

    def _readfile(self):
        """Return a list of lines without \n and without line with comments"""
        with open(self.filename) as opened_file:
            return [line.strip() for line in opened_file
                                    if line.strip() and '#' not in line[0]]

    def _readfile_inblocks(self):
        """Return blocks of the file"""
        with open(self.filename) as opened_file:
            tmp = [tuple(group) for key, group in groupby(opened_file,
                                                lambda line: line == '\n')]

        return [line for line in tmp if len(line) > 1]

    def _writefile(self, line):
        """Just writes a line in a file"""
        with open(self.filename, 'w+') as opened_file:
            opened_file.write(line)
