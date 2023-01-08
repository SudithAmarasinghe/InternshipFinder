import subprocess

cmd = 'python registation_form.py'
p = subprocess.Popen(cmd,shell=True)
p.communicate()