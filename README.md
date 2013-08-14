proc
====
proc is a collection of python scripts that parses the /proc of Linux systems.  
The idea is to have a ground to develop tools like vmstat, iotop etc, but using python.  

This is a work in progress, I hope this can be helpful for more people.

How to Use
==========
import proc
>>> proc.vmstat.nr_free_pages
80984
>>> proc.vmstat.unevictable_pgs_munlocked
20
>>> proc.process[24174].oom_score
'0'
>>> proc.process[24174].pid
24174
>>> proc.process[24174].cmdline
['/usr/bin/fish']
>>> proc.process[24174].comm
'fish'
>>> proc.filesystems.ext4.used
True
>>> proc.filesystems.mqueue.used
False
>>> proc.meminfo.memfree
323936
>>> proc.meminfo.swapcached
0
>>> proc.meminfo.shmem
418644
>>> proc.modules.ip6_tables.state
'Live'
>>> proc.modules.ip6_tables.memory_size
22050
>>> proc.modules.ip6_tables.instances_counter
1
>>> proc.consoles.tty0.operations
'-WU'
>>> proc.consoles.tty0.flags
'ECp'
>>> proc.consoles.tty0.major
'4'
>>> proc.consoles.tty0.minor
'7'
>>> proc.diskstats.sda1.reads
191
>>> proc.diskstats.sda2.reads
177
