import subprocess
import csv
import datetime
import os
import numpy as np

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

##### B up data files
## Copy CSV files with frame timestamps
copy_csv_from = str("/home/gustavo/TITS/VIDEOS/")
copy_csv_to = str("/run/user/1001/gvfs/smb-share:server=r-zfssvr01,share=grplucy/Videos_GRETI/")

##  GEt a list of files in original folder
files_from = os.listdir(copy_csv_from)
#print(files_from)

##  GEt a list of files in backup folder
files_bup = os.listdir(copy_csv_to)

files_to_bup = np.setdiff1d(files_from, files_bup)
print(files_to_bup)

#Copy Video files
for i in (files_to_bup):
    #print("es " + i)
    copy_str = str('mv ' + "/home/gustavo/TITS/VIDEOS/" + str(i) + ' ' + "/run/user/1001/gvfs/smb-share:server=r-zfssvr01,share=grplucy/Videos_GRETI/")
    #print(copy_str)
    terminal(copy_str)

##### B up RAW video files

## Copy video files with frame timestamps
#copy_from = str("/home/gustavo/COCKATIELS/VIDEOS/DONE/")

#copy_to = str("/run/user/1001/gvfs/smb-share:server=r-zfssvr01,share=grplucy/Gustavo/VIDEOS/DONE/")

##  Get a list of files in original folder
#files_from = os.listdir(copy_from)
#print(files_from)

##  GEt a list of files in backup folder
#files_bup = os.listdir(copy_to)

#files_to_bup = np.setdiff1d(files_from, files_bup)
#print(files_to_bup)

#Copy files
#for i in (files_to_bup):
    #print("es " + i)
 #   copy_str = str('cp -r ' + copy_from + str(i) + ' ' + copy_to)
  #  print("copying " + i)
   # print(copy_str)
    #terminal(copy_str)

