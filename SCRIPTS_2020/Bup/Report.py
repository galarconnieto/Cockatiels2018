from PIL import Image

#!/bin/bash/
import subprocess
import csv
import datetime
#import psutil
import os
import cv2
import time
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
for i in range(0, (len(ip_pi))):  # (0, (len(ip_pi_-1): #use this for more than one pi
    #Folder of current day's photos
    abc1= str("ssh " + ip_pi[i] + " ls " + "APAPORIS/MOVED/*.*")
    print(ip_pi[i])

    #target_folder1 = str(pi_name[i] + str('_{:%Y-%m-%d}'.format(datetime.datetime.now())))
    #copy_from = str("/home/pi/APAPORIS/MOVED/" + target_folder + "/")
    files_in_pi = str("ssh " + ip_pi[i] + " ls " + "COCKATIELS/PHOTOS/" + target_folder + "/ -l | grep ^- | wc -l")
    
    files1 = terminal(files_in_pi)
    files1 = files1[:-1]
    print(files1)
    #time.sleep(15)
    #files2 = str("ssh " + ip_pi[i] + " ls " + "COCKATIELS/PHOTOS/" + target_folder + "/ -l | grep ^- | wc -l")
    #files2 = terminal(files2)
    #files2 = files2[:-1]
    if files1 != files2:
        
        #copy_str = str('scp -r ' + ip_pi[i] + ':' + copy_from + ' ' + copy_to)
        last_file_com = str("ssh " + ip_pi[i] + " ls " + copy_from + " | tail --lines=1")
        last_photo = str(terminal(last_file_com))
        last_photo = last_photo[:-1]
        message = (str("This is the last photo     Total photos = ") + str(files2))
        print(message)
        copy_str_last = str('scp ' + ip_pi[i] + ':' + copy_from + last_photo + ' ' + "/home/gustavo/COCKATIELS/REPORTS/")
        #print("Close with ESC key")
        terminal(copy_str_last)
        img=Image.open("/home/gustavo/COCKATIELS/REPORTS/" + last_photo)
        img=img.resize((380, 240))
        img = img.save("/home/gustavo/COCKATIELS/REPORTS/" + last_photo)
        #img.show()
        texto = (str("echo \"" + message + "\" > /home/gustavo/COCKATIELS/REPORTS/text"))
        print(texto)
        terminal(texto)
        emailme= str("mpack -s Loros -d /home/gustavo/COCKATIELS/REPORTS/text /home/gustavo/COCKATIELS/REPORTS/" + last_photo + " galarconnieto@orn.mpg.de")
        print(emailme)
        terminal(emailme)
    else:
        rebooting = str('ssh ' + ip_pi[i] + " sudo reboot")
        print(rebooting)
        terminal(rebooting)
        time.sleep(200)
        restart_photos = str('ssh ' + ip_pi[i] + " python /home/pi/COCKATIELS/SCRIPTS/Photos_Outdoors3.py")
        terminal(restart_photos)
        files1 = str("ssh " + ip_pi[i] + " ls " + "COCKATIELS/PHOTOS/" + target_folder + "/ -l | grep ^- | wc -l")
    
        files1 = terminal(files1)
        files1 = files1[:-1]
        print(files1)
        time.sleep(20)
        files2 = str("ssh " + ip_pi[i] + " ls " + "COCKATIELS/PHOTOS/" + target_folder + "/ -l | grep ^- | wc -l")
        files2 = terminal(files2)
        files2 = files2[:-1]
        if files1 != files2:
            
            #copy_str = str('scp -r ' + ip_pi[i] + ':' + copy_from + ' ' + copy_to)
            last_file_com = str("ssh " + ip_pi[i] + " ls " + copy_from + " | tail --lines=1")
            last_photo = str(terminal(last_file_com))
            last_photo = last_photo[:-1]
            message = (str("Rebooted after failure     Total photos = ") + str(files2))
            print(message)
            copy_str_last = str('scp ' + ip_pi[i] + ':' + copy_from + last_photo + ' ' + "/home/gustavo/COCKATIELS/REPORTS/")
            #print("Close with ESC key")
            terminal(copy_str_last)
            img=Image.open("/home/gustavo/COCKATIELS/REPORTS/" + last_photo)
            img=img.resize((380, 240))
            img = img.save("/home/gustavo/COCKATIELS/REPORTS/" + last_photo)
            #img.show()
            texto = (str("echo \"" + message + "\" > /home/gustavo/COCKATIELS/REPORTS/text"))
            print(texto)
            terminal(texto)
            emailme= str("mpack -s Loros -d /home/gustavo/COCKATIELS/REPORTS/text /home/gustavo/COCKATIELS/REPORTS/" + last_photo + " galarconnieto@orn.mpg.de")
            #print(emailme)
            terminal(emailme)
        else:
            texto = (str("echo \"" + "failure" + "\" > /home/gustavo/COCKATIELS/REPORTS/text"))
            print(texto)
            terminal(texto)
            emailme= str("mpack -s Loros -d /home/gustavo/COCKATIELS/REPORTS/text /home/gustavo/COCKATIELS/REPORTS/" + last_photo + " galarconnieto@orn.mpg.de")
            #print(emailme)
            terminal(emailme)


    


