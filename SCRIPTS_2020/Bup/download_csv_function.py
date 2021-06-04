#!/bin/bash/
import subprocess
import csv
import datetime
#import psutil
import os

##def terminal(line):
##    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
##    return command.stdout.read()

we=str('eval ' + 'ssh-agent')
os.system(we)
ip_pi = str('pi@10.76.0.91')
target_folder = 123


copy_from = str("/home/pi/COCKATIELS/SCRIPTS/")
copy_to = str("/home/gustavo/COCKATIELS/PHOTOS/")

#Copy files from Raspbery pi
copy_str = str('scp -r ' + ip_pi + ':' + copy_from + '*.csv ' + copy_to)
#print(copy_str)
os.system(copy_str)
