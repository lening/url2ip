import re
import os
if os.path.exists('result.txt'):
	os.remove('result.txt')
sfile=open("url.txt")
for line in sfile:
	cmd="nslookup "+line
	result=os.popen(cmd)
	for line in result.readlines()[3:]:
		p=re.search("[0-9][0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",line)
		if p != None:
			with open("result.txt","a") as dfile:
				dfile.write(p.group(0))
				dfile.write('\n')
sfile.close()