import os
from basic import ProcFile
from collections import namedtuple

class IO(ProcFile):
    def __init__(self, pid):
        ProcFile.__init__(self)
        self.filename = '/proc/%s/io' % pid

    def names(self):
        return [line.split(':')[0] for line in self._readfile()]

    def get(self, name, default = None):
        for line in self._readfile():
            info = line.split(':')
            if name == info[0]:
                return int(info[1])

            else:
                None

    def __getattr__(self, name):
        if name in self.names():
            return self.get(name)

        else:
            raise AttributeError 
        

class PId(object):
    Stat = namedtuple( 'Stat', ['pid', 'comm', 'state', 'ppid', 'pgrp', 'session', 'tty_nr','tpgid',
            'flags', 'minflt', 'cminflt', 'majflt', 'cmajflt', 'utime','stime',
            'cutime', 'cstime', 'priority', 'nice', 'num_threads', 'itrealvalue',
            'starttime', 'vsize', 'rss', 'rsslim', 'startcode', 'endcode', 'startstack',
            'kstkesp', 'kstkeip', 'signal', 'blocked', 'sigignore', 'sigcatch',
            'wchan', 'nswap', 'cnswap', 'exit_signal', 'processor', 'rt_priority',
            'policy', 'delayacct_blkio_ticks', 'guest_time', 'cguest_time', 'start_data',
            'end_data', 'start_brk', 'arg_start', 'arg_end', 'env_start', 'env_end'])

    def __init__(self, pid):
        self.pid = pid
        #Generic Proc File
        self.gpf = ProcFile()

    @property
    def id_(self):
        return self.pid

    @property
    def oom_score(self):
        self.gpf.filename = '/proc/%s/oom_score' % self.pid
        score = self.gpf._readfile()
        return score[0]

    @property
    def oom_adj(self):
        self.gpf.filename = '/proc/%s/oom_adj' % self.pid
        score = self.gpf._readfile()
        return score[0]

    @oom_adj.setter
    def oom_adj(self, line):
        self.gpf.filename = '/proc/%s/oom_adj' % self.pid
        self.gpf._writefile(str(line))

    @property
    def oom_score_adj(self):
        self.gpf.filename = '/proc/%s/oom_score_adj' % self.pid
        score = self.gpf._readfile()
        return score[0]

    @oom_score_adj.setter
    def oom_score_adj(self, line):
        self.gpf.filename = '/proc/%s/oom_score_adj' % self.pid
        self.gpf._writefile(str(line))

    @property
    def cpuset(self):
        self.gpf.filename = '/proc/%s/cpuset' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @property
    def sessionid(self):
        self.gpf.filename = '/proc/%s/sessionid' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @property
    def personality(self):
        self.gpf.filename = '/proc/%s/personality' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @property
    def coredump_filter(self):
        self.gpf.filename = '/proc/%s/coredump_filter' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @coredump_filter.setter
    def coredump_filter(self, line):
        self.gpf.filename = '/proc/%s/coredump_filter' % self.pid
        self.gpf._writefile(str(line))

    @property
    def cmdline(self):
        self.gpf.filename = '/proc/%s/cmdline' % self.pid
        value = self.gpf._readfile()
        return value[0].split('\0')[:-1]

    @property
    def environ(self):
        self.gpf.filename = '/proc/%s/environ' % self.pid
        value = self.gpf._readfile()
        return value[0].split('\0')[:-1]

    @property
    def exe(self):
        return os.readlink('/proc/%s/exe' % self.pid)

    @property
    def comm(self):
        self.gpf.filename = '/proc/%s/comm' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @property
    def cpuset(self):
        self.gpf.filename = '/proc/%s/cpuset' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @property
    def cwd(self):
        return os.readlink('/proc/%s/cwd' % self.pid)

    @property
    def io(self):
        return IO(self.pid)

    @property
    def loginuid(self):
        self.gpf.filename = '/proc/%s/loginuid' % self.pid
        value = self.gpf._readfile()
        return value[0]

    @loginuid.setter
    def loginuid(self, line):
        self.gpf.filename = '/proc/%s/loginuid' % self.pid
        self.gpf._writefile(str(line))

    @property
    def stat(self):
        self.gpf.filename = '/proc/%s/stat' % self.pid
        values = self.gpf._readfile()[0].split()
        pid = int(values[0])
        comm = values[1]
        state = values[2]
        tmp_tuple = tuple(map(int, values[4:52]))
        if len(values) < 51:
            values.extend([]*(51 - len(values)))
            
        stat = self.Stat(pid, comm, state, *tmp_tuple)

        return stat


class Process(object):
    directory = '/proc'

    def names(self):
        return ['p%s' % pid for pid in os.listdir(self.directory) if pid.isdigit()]

    def __getattr__(self, name):
        if name in self.names():
            return PId(name.replace('p',''))

        else:
            raise AttributeError


if __name__ == '__main__':
    process = Process()
#    print process.names()
#    print process.p1
    print process.p1.id_
    print process.p1.oom_score
    print process.p12745.oom_adj
    process.p12745.oom_adj = 1
    print process.p12745.oom_adj
    print process.p12745.oom_score_adj
    process.p12745.oom_score_adj = 0
    print process.p12745.oom_score_adj
    print process.p12745.cpuset
    print process.p12745.sessionid
    print process.p12745.personality
    print process.p12745.coredump_filter
    print process.p12745.cmdline
    print process.p12745.environ
    print process.p12745.exe
    print process.p12745.comm
    print process.p12745.cpuset
    print process.p12745.cwd
    print process.p12745.io.rchar
    print process.p12745.io.read_bytes
    print process.p12745.loginuid
    print process.p12745.stat.pid
    print process.p12745.stat.comm
    print process.p12745.stat.guest_time
    print process.p12745.stat.rss
    print process.p12745.stat.vsize
    print process.p12745.stat.processor
