import os
import re
cmd = "ps -eo pcpu,pid | sort -k1 -r -n | head -1"
s = str(os.popen(cmd).read())
s= s.split()
pid = int(s[1])
i = int(float(s[0]))
print(i)
if(i > 60):
  kills = 'kill -9 '+str(pid)
  print(kills)
  os.system(kills)
  




  
