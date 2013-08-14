from basic import ProcFile
from collections import namedtuple

class SoftIrqs(ProcFile):
    filename = '/proc/softirqs'
    SoftIrq = namedtuple('SoftIrq', ['hi', 'timer', 'net_tx', 'net_rx',
                                    'block', 'block_iopoll', 'tasklet',
                                    'sched', 'hrtimer', 'rcu'])

    def names(self):
        return [field.lower() for field in self._readfile()[0].split()]

    def get(self, cpu_name, default = None):
        info = self._readfile()
        try:
            header = info.pop(0).split()
            field = header.index(cpu_name.upper()) + 1
            return [line.split()[field] for line in info]

        except ValueError:
            return default

    def __getattr__(self, name):
        if name in self.names():
            (hi, timer, net_tx, net_rx,
            block, block_iopoll, tasklet,
            sched, hrtimer, rcu) = tuple(map(int, self.get(name)))

            return self.SoftIrq(hi, timer, net_tx, net_rx,
                           block, block_iopoll, tasklet,
                           sched, hrtimer, rcu)

        else:
            raise AttributeError


if __name__ == '__main__':
    softirqs = SoftIrqs()
    print softirqs.names()
    print softirqs.get('cpu1')
    print softirqs.cpu1.timer
