import subprocess

cmd = 'python registration_form.py'
p = subprocess.Popen(cmd,shell=True)
p.communicate()

