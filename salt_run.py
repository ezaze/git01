#import commands
import subprocess
import sys
print sys.argv[1]
# subprocess.call('/usr/bin/salt ' + sys.argv[1] +' cmd.run "ip a"',shell=True)
subprocess.call('/usr/bin/ping -c 3 ' + sys.argv[1],shell=True)
#subprocess.call('ping -c 3 ' + sys.argv[1], shell=True)
#print '/usr/bin/salt ' + sys.argv[1] + 'cmd.run "ip a"'
#a,b = commands.getstatusoutput('/usr/bin/ping ' + sys.argv[1])
#a,b = commands.getstatusoutput('/usr/bin/salt ' + sys.argv[1] + ' cmd.run "ip a"')
