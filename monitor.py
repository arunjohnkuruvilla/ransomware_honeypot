import psutil
import time
import sys
import os
import subprocess
import threading
import re

safe_pids = []
def monitor(regex):
	
	global safe_pids
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid'])
		except psutil.NoSuchProcess:
			pass
		else:
			try:
				proci = psutil.Process(pinfo['pid'])
				for files in proci.open_files() :
					#print files.path
					#handles = re.match(my_regex, files, re.IGNORECASE)
					print files.path
					match = regex.search(str(files))
					if match is not None:
						'''
						if file in files.path:
						
						if pinfo['pid'] in safe_pids:
							return False, 0
						else:
							safe_pids.append(pinfo['pid'])
							return True, pinfo['pid']
						'''
						sys.stdout.write('\a')
						print "File being accessed at" + time.ctime() + " by process " + str(pinfo['pid'])
						'''
						proci.suspend()
						
						offpid = pinfo['pid']

						randdump = str(time.time()) + str(offpid) + ".dmp" ;
				
						dumpcmd = os.path.dirname(sys.executable) + "\\" + 'procdump.exe -ma ' + "\"" + str(offpid) + "\"" + ' -accepteula ' + randdump
					
						cmdblock =subprocess.Popen(dumpcmd, stdout=subprocess.PIPE)
						cmdblock.wait()
						
						p.kill()	
						'''
						return True
					
					#print match

			except:
				pass

	return False

def main():
	while True:
		my_regex = r".*" + re.escape(sys.argv[1]) + r".*"
	
		regex = re.compile(my_regex, re.IGNORECASE)

		status = monitor(regex)
		if status == True:
			return	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print e
		print 'Exiting Monitor.'