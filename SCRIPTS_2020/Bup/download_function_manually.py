#!/bin/bash/
import subprocess
import csv
import datetime
#import psutil
import os

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

# list of ip addresses
pis = [0,1]
ip_pi = ['pi@10.76.0.105']
pi_name = ['Puzzle_P2_C3']
#print(len(ip_pi))




#copy_to = str("TITS/PHOTOS/" + pi_name + target_folder + "/")



##if not os.path.exists(copy_to):
##    os.makedirs(copy_to)

### COPY PHOTOS AND CSV TO TOWER/DELETE FROM PI
for i in pis: # (0, (len(ip_pi_-1): #use this for more than one pi
    #Folder of current day's photos
    abc1= str("ssh " + ip_pi[i] + " ls " + "APAPORIS/PHOTOS/" + " | head --lines=1")
    target_folder = terminal(str(abc1))
    target_folder = target_folder[:-1]


    #target_folder1 = str(pi_name[i] + str('_{:%Y-%m-%d}'.format(datetime.datetime.now())))
    copy_from = str("APAPORIS/PHOTOS/" + target_folder + "/")

    #print(i)
    ip = ip_pi[i]
    #print(ip)
    pi_curr_name = pi_name[i]
    #print(pi_curr_name)
    copy_to = str("TITS/PHOTOS/" + target_folder + "/")
    #print(target_folder)
    count_files_copy_from = terminal(str("ssh " + ip + " ls " + copy_from + ' | wc -l' ))
    #print(count_files_copy_from)

    #Copy files from Raspbery pi
    copy_str = str('scp -r ' + ip + ':' + copy_from + ' ' + copy_to)
    terminal(copy_str)
    count_files_copy_to = terminal(str("ls " + copy_to + ' | wc -l' ))
    print(count_files_copy_from)

    if count_files_copy_from == count_files_copy_to:
        move_command = str('ssh ' + ip + " mv " + copy_from + str(" TITS/MOVED/" + target_folder + "/"))
        terminal(move_command)
        ## remove files from pi
        remove_command = str('ssh ' + ip + ' rm -rf' + ' APAPORIS/MOVED/' + target_folder + '/')
        terminal(remove_command)

        
    ## Copy CSV files with frame timestamps
    copy_csv_from = str("/home/pi/TITS/SCRIPTS/")
    copy_csv_to = str("/home/gustavo/TITS/CSV/")

    #Copy CSV files from Raspbery pi
    copy_csv_str = str('scp -r ' + ip + ':' + copy_csv_from + '*.csv ' + copy_csv_to)
    #print(copy_str)
    os.system(copy_csv_str)

    a_video = str('ffmpeg -r 24 -i ' + copy_to + target_folder + '_%05d.jpg ' + "TITS/VIDEOS/TO_PROCESS/" + target_folder + '.MP4')
    terminal(a_video)
    #print(a_video)



