from basic import ProcFile
from collections import namedtuple

class DiskStats(ProcFile):
    filename = '/proc/diskstats'
    DiskStat = namedtuple('DiskStat', ['major', 'minor', 
                                       'reads', 'reads_merged',
                                       'read_sectors', 
                                       'time_reading', 'writes',
                                       'writes_merged', 'written_sectors',
                                       'time_writing', 'current_io_progress',
                                       'time_io', 'time_io_since_last_update'])

    @property
    def value(self):
        return ' '.join(self._readfile())

    def names(self):
        return [line.split()[2] for line in self._readfile()]

    def get(self, disk_name, default = None):
        for line in self._readfile():
            disk_info = line.split()
            if disk_name == disk_info[2]:
                disk_info.pop(2)
                return disk_info

        else:
            return default

    def __getattr__(self, name):
        if name in self.names():
            (major, minor, 
            reads, reads_merged,
            read_sectors,
            time_reading, writes,
            writes_merged, written_sectors,
            time_writing, current_io_progress,
            time_io, time_io_since_last_update) = tuple(self.get(name))

            return self.DiskStat(int(major), int(minor),
                                int(reads), int(reads_merged),
                                int(read_sectors), int(time_reading),
                                int(writes), int(writes_merged),
                                int(written_sectors), int(time_writing),
                                int(current_io_progress), int(time_io),
                                int(time_io_since_last_update))

        else:
            raise AttributeError


if __name__ == '__main__':
    diskstats = DiskStats()
#    print(diskstats.value)
    print(diskstats.names())
    print(diskstats.get('sda1'))
    print diskstats.sda.major
    print diskstats.sda.minor
    print diskstats.sda.reads
    print diskstats.sda.writes
    print diskstats.sda.time_io_since_last_update

