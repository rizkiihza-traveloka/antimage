import subprocess

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = []
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        result.append(line)
        if retcode is not None:
            break
        
    return result