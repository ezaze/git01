import commands
import sys
print sys.argv[1]
print '/usr/bin/salt ' + sys.argv[1] + 'cmd.run "ip a"'
a,b = commands.getstatusoutput('/usr/bin/salt ' + sys.argv[1] + ' cmd.run "ip a"')
print b
