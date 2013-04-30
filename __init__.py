from cmdline import CMDLine
from modules import Modules
from filesystems import Filesystems
from cgroups import CGroups
from diskstats import DiskStats
from stat import Stat
from softirqs import SoftIrqs
from uptime import Uptime
from loadavg import LoadAvg
from version import Version
from vmstat import VMStat

cmdline = CMDLine()
modules = Modules()
filesystems = Filesystems()
cgroups = CGroups()
diskstats = DiskStats()
stat = Stat()
softirqs = SoftIrqs()
uptime = Uptime()
loadavg = LoadAvg()
version = Version()
vmstat = VMStat()
