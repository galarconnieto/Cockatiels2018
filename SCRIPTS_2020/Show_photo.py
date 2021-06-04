#!/bin/bash/
import subprocess
import csv
import datetime
from ipsandnames import ip_pi
from ipsandnames import pi_name
#import psutil
import os
import cv2

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

# list of ip addresses
#ip_pi = ['pi@10.0.20.184', 'pi@10.76.0.92']
#pi_name = ['office', 'Feeder_C2']

pis = list(range(len(ip_pi)))
#print(pis)
#print(pis)

#copy_to = str("COCKATIELS/PHOTOS/" + pi_name + target_folder + "/")
#if not os.path.exists(copy_to):
##    os.makedirs(copy_to)

### COPY PHOTOS AND CSV TO TOWER/DELETE FROM PI
for i in pis: #(0, (len(ip_pi_-1): #use this for more than one pi
    #Folder of current day's photos
    abc1= str("ssh " + ip_pi[i] + " ls " + "APAPORIS/PHOTOS/" + " | tail --lines=1")
    print(ip_pi[i])
    print(pi_name[i])

    target_folder = terminal(str(abc1))
    target_folder = target_folder[:-1]
    #print(target_folder)


    target_folder1 = str(pi_name[i] + str('_{:%Y-%m-%d}'.format(datetime.datetime.now())))
    copy_from = str("/home/pi/APAPORIS/PHOTOS/")# + target_folder + "/")
    #copy_str = str('scp -r ' + ip_pi[i] + ':' + copy_from + ' ' + copy_to)
    last_file_com = str("ssh " + ip_pi[i] + " ls " + copy_from + " | tail --lines=1")
    last_photo = str(terminal(last_file_com))
    last_photo = last_photo[:-1]
    print(str("This is the last_photo"))
    copy_str_last = str('scp ' + ip_pi[i] + ':' + copy_from + last_photo + ' ' + "/home/gustavo/TITS/REPORTS/")
    print("Hit any key to close")
    terminal(copy_str_last)
    img = cv2.imread(str("TITS/REPORTS/" + last_photo))
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 1900, 1200)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
