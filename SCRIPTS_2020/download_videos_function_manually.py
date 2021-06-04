#!/bin/bash/
import subprocess
import csv
import datetime
#import psutil
import os
from ipsandnames import ip_pi
from ipsandnames import pi_name

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

# list of ip addresses
#ip_pi = ['pi@10.76.0.92']
#pi_name = ['Feeder_C2']
pis = list(range(len(ip_pi)))
#print(pis)

#copy_to = str("COCKATIELS/PHOTOS/" + pi_name + target_folder + "/")
#if not os.path.exists(copy_to):
##    os.makedirs(copy_to)

### COPY PHOTOS AND CSV TO TOWER/DELETE FROM PI
if True: #, (len(ip_pi))):  #use this for more than one pi
    #pii = ip_pi[i]
    #pii = pii[3:14]
    pii = str('10.76.0.202')
	
    try:
        abc = str("ping -c2 "+ pii)
        print(abc)
        response = terminal(abc)
        print(response)
        #print("a")
        if "2 received, 0% packet loss" in response:
            
		#Folder of current day's videos
            abc1= str("ssh pi@" + pii + " ls " + "APAPORIS/MOVED/*.h264")# + " | head --lines=1")
            print(abc1)

            #target_folder = terminal(str(abc1))
            #target_folder = target_folder[:-1]
            #print("target folder" + target_folder)


            #target_folder1 = str(pi_name[i] + str('_{:%Y-%m-%d}'.format(datetime.datetime.now())))
            copy_from = str("APAPORIS/MOVED/")# + target_folder + "/")

            #print(i)
            ip = str('pi@' + pii)
            print(ip)
            #pi_curr_name = pi_name[i]
            #print(pi_curr_name)
            copy_to = str("TITS/VIDEOS/")# + target_folder + "/")
            print(copy_to)
            count_files_copy_from = terminal(str("ssh " + ip + " ls " + copy_from + ' | wc -l' ))
            #print(count_files_copy_from)

            #Copy files from Raspbery pi
            copy_str = str('scp ' + ip + ':' + copy_from + '*.* ' + copy_to)
	    print(copy_str)
            terminal(copy_str)
            count_files_copy_to = terminal(str("ls " + copy_to + ' | wc -l' ))
            print(count_files_copy_from)

            if  True: #count_files_copy_from == count_files_copy_to:
                #move_command = str('ssh ' + ip + " mv " + copy_from + str(" TITS/VIDEOS/"))# + target_folder + "/"))
                #terminal(move_command)
                ## remove files from pi
                remove_command = str('ssh ' + ip + ' rm -rf' + ' APAPORIS/MOVED/*.h264')# + target_folder + '/')
                terminal(remove_command)

                
            ## Copy CSV files with frame timestamps
            #copy_csv_from = str("/home/pi/APAPORIS/CSV/")
            #copy_csv_to = str("/home/gustavo/TITS/CSV/")

            #Copy CSV files from Raspbery pi
            #copy_csv_str = str('scp -r ' + ip + ':' + copy_csv_from + '*.csv ' + copy_csv_to)
            #print(copy_str)
            #os.system(copy_csv_str)

            #a_video = str('ffmpeg -r 24 -i ' + copy_to + target_folder + '_%05d.jpg ' + "TITS/VIDEOS/TO_PROCESS/" + target_folder + '.MP4')
            #terminal(a_video)
            #print(a_video)
		





##    count_files_copy_to = terminal(str("ls " + copy_to + ' | wc -l' ))
##    print(count_files_copy_from)

            

                        
        else:
            print(pii+" Unreachable")
        #print("a")

        #print('\n'.join(response.split('\n')[8:]))


    except:
        print("Invalid Hostname")










    



