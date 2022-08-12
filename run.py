import os
import time
import subprocess

pid_list = []
res1 = subprocess.Popen("cd cl_system; python3 main/web_app.py", shell=True)
time.sleep(5)
res2 = subprocess.Popen("cd cl-frontend; npm start", shell=True)
time.sleep(5)
pid_list.append(res1.pid)
pid_list.append(res2.pid)

msg = input("press ENTER to end the process\n")
web_app_pid = os.popen("ps -aux | grep -v grep | grep 'web_app' | awk '{print $2}'")
web_app_pid = web_app_pid.readlines()
for pid in web_app_pid:
    if pid not in pid_list:
        pid_list.append(pid.strip())
front_end_pid = os.popen("ps -aux | grep -v grep | grep 'start.js' | awk '{print $2}'")
front_end_pid = front_end_pid.readlines()
for pid in front_end_pid:
    if pid not in pid_list:
        pid_list.append(pid.strip())


for pid in pid_list:
    os.system("kill"+" "+str(pid))
os.system("\n")
