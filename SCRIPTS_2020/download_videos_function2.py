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



### MOVE VIDEOS TO TRANSFER FOLFER ON PI
for i in range(12, (len(ip_pi))):  #use this for more than one pi
    pii = ip_pi[i]
    pii = pii[3:14]
    
	
    try:
        abc = str("ping -c2 "+ pii)
        #print(abc)
        response = terminal(abc)
        #print(response)
        #print("a")
        if "2 received, 0% packet loss" in response:
            
		#Folder of current day's videos
            #abc1= str("ssh " + ip_pi[i] + " ls " + "APAPORIS/MOVED/*.*")# + " | head --lines=1")
            #print(abc1)

            #target_folder = terminal(str(abc1))
            #target_folder = target_folder[:-1]
            #print("target folder" + target_folder)


            #target_folder1 = str(pi_name[i] + str('_{:%Y-%m-%d}'.format(datetime.datetime.now())))
            copy_from = str("APAPORIS/MOVED/")# + target_folder + "/")
            copy_to = str("APAPORIS/TO_TRANSFER/")# + target_folder + "/")

            #print(i)
            ip = ip_pi[i]
            #print(ip)
            pi_curr_name = pi_name[i]
            #print(pi_curr_name)
            count_files_copy_from = terminal(str("ssh " + ip + " ls " + copy_from + ' | wc -l' ))
            
            #print(count_files_copy_from)
            #count_files_copy_from = terminal(str("ssh " + ip + " ls " + copy_from + ' | wc -l' ))
            #print(count_files_copy_from)

            #Copy files from Raspbery pi
            copy_str = str('ssh ' + ip + ' mv ' + copy_from + '*.* ' + copy_to)
	    #print(copy_str)
            terminal(copy_str)
            count_files_copy_to = terminal(str('ssh ' + ip + " ls " + copy_to + ' | wc -l' ))
            #print(count_files_copy_to)
       
        else:
            print(pii+" Unreachable")
        #print("a")

        #print('\n'.join(response.split('\n')[8:]))

    except:
         print("Invalid Hostname")

#print("ready to download")



### COPY PHOTOS AND CSV TO TOWER/DELETE FROM PI
for i in range(12, (len(ip_pi))):  #use this for more than one pi
    pii = ip_pi[i]
    pii = pii[3:14]
    target_folder = str(pi_name[i] + str('_{:%Y-%m-%d_%H}'.format(datetime.datetime.now())))
	
    try:
        abc = str("ping -c2 "+ pii)
        #print(abc)
        response = terminal(abc)
        #print(response)
        #print("a")
        if "2 received, 0% packet loss" in response:
            
		#Folder of current day's videos
            abc1= str("ssh " + ip_pi[i] + " ls " + "APAPORIS/TO_TRANSFER/*.*")# + " | head --lines=1")
         #   print(abc1)

            #target_folder = terminal(str(abc1))
            #target_folder = target_folder[:-1]
            #print("target folder" + target_folder)
            
          #  print(target_folder)
            copy_from = str("APAPORIS/TO_TRANSFER/")# + target_folder + "/")

            #print(i)
            ip = ip_pi[i]
            print("Downloading from " + ip) # print(ip)
            pi_curr_name = pi_name[i]
            #print(pi_curr_name)
            copy_to = str("TITS/VIDEOS/" + target_folder + "/")
            #print(copy_to)
            count_files_copy_from = terminal(str("ssh " + ip + " ls " + copy_from + ' | wc -l' ))
            #print(count_files_copy_from)

            #Copy files from Raspbery pi
            abc1= str("mkdir -v" + " ./" + copy_to)
            #print(abc1)
            terminal(abc1)
            copy_str = str('scp ' + ip + ':' + copy_from + '*.* ' + copy_to)
	    #print(copy_str)
            terminal(copy_str)
            count_files_copy_to = terminal(str("ls " + copy_to + ' | wc -l' ))
            #print(count_files_copy_from)


            if  count_files_copy_from == count_files_copy_to:
                remove_command = str('ssh ' + ip + ' rm -rf' + ' APAPORIS/TO_TRANSFER/*.*')
                terminal(remove_command)

                #move_command = str('ssh ' + ip + " mv " + copy_from + str(" TITS/VIDEOS/"))# + target_folder + "/"))
                #terminal(move_command)
                ## remove files from pi

                
                      
        else:
            print(pii+" Unreachable")
        #print("a")

        #print('\n'.join(response.split('\n')[8:]))


    except:
        print("Invalid Hostname")

print('Done')







    



