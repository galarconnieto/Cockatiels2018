#!/bin/bash/
import subprocess
import csv
import datetime
#import psutil
import os

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

ip_pi = str('pi@10.76.0.91')


##abc= str("ssh " + ip_pi + " ls -1 " + "COCKATIELS/PHOTOS/" + " | wc -l")
##print(abc)
##number_of_folders = int(terminal(abc))
##print(number_of_folders)
##if number_of_folders == 2:
##
##    abc1= str("ssh " + ip_pi + " ls " + "COCKATIELS/PHOTOS/" + " | head --lines=1")        
##    #print(abc1)
##    target_folder = terminal(str(abc1))
##    #print(target_folder)
##    target_folder = str(target_folder)
##
##    target_folder = str(target_folder[11:23])
##
##    print(str('name is ') + target_folder)
#target_folder = str('2018-06-16')
#print(str('name is ') + target_folder)
abc1= str("ssh " + ip_pi + " ls " + "COCKATIELS/PHOTOS/" + " | head --lines=1")
target_folder = terminal(str(abc1))
target_folder = target_folder[:-1]

copy_from = str("COCKATIELS/PHOTOS/" + target_folder + "/")

copy_to = str("COCKATIELS/PHOTOS/" + target_folder + "/")



##if not os.path.exists(copy_to):
##    os.makedirs(copy_to)



count_files_copy_from = str("ssh " + ip_pi + " ls " + copy_from + ' | wc -l' )
#print(count_files_copy_from)
num_files_remote = int(os.system(count_files_copy_from ))
#Copy files from Raspbery pi
copy_str = str('scp -r ' + ip_pi + ':' + copy_from + ' ' + copy_to)
terminal(copy_str)


###Copy files from Raspbery pi
##copy_str = str('scp -r ' + ip_pi + ':' + copy_from + ' ' + copy_to)
##print(copy_str)
##
##count_files_copy_to = str("ls " + copy_to + ' | wc -l' )
##print(count_files_copy_to)
##num_files_local = int(os.system(count_files_copy_to))
##print(num_files_local)
###os.system(copy_str)
##
##count_files_copy_to = str("ls " + copy_to + ' | wc -l' )
##print(count_files_copy_to)
##num_files_local = int(os.system(count_files_copy_to))
##print(num_files_local)
##
##if num_files_local == num_files_remote:
##    ocho = str('remove')
##    print(ocho)
##    ocho = ocho[2:5]
##    print(ocho)  
##
##    #move_command = (str('ssh ' + ip_pi + " mv " + copy_from + str(" COCKATIELS/MOVED/" + target_folder + "/")))
##    #terminal(str(move_command))
##
####photo_to_video
####photo_to_video = str('ffmpeg -r 24 image2 -i ' + copy_to + target_folder + '_%05d.jpg' + target_folder +'.MP4')
####print(photo_to_video)
####
####terminal(photo_to_video)
