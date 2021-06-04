#!/bin/bash/
import barcode_tracker_tits as tracker
#import barcode_tracker_gopro as tracker
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from scipy.spatial import distance as dist

from pinpoint import TagDictionary as TagList
import glob
import os
import pickle
import subprocess
import time
#%matplotlib inline
##get_ipython().magic(u'matplotlib inline')
##cv2.setNumThreads(0) # Turn off multithreading to prevent errors
##print "packages loaded"

def terminal(line):
    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
    return command.stdout.read()

count_files = terminal(str("ls Cockatiels/VIDEOS/TO_PROCESS/ | wc -l" ))

while count_files > 0:

    abc1 = str("ls " + "Cockatiels/VIDEOS/TO_PROCESS/" + " | head --lines=1")
    Curr_video1 = terminal(abc1)
    print(Curr_video1)
    time.sleep(20)
    b = terminal(abc1)
    print(b)
    if b == Curr_video1:
        Curr_video = Curr_video1[:-5]
    else: break

    move_command = str("mv /home/gustavo/Cockatiels/VIDEOS/TO_PROCESS/" + Curr_video + ".MP4 /home/gustavo/Cockatiels/VIDEOS/PROCESSING/")
    #print(move_command)
    terminal(move_command)

    print(Curr_video)
    #print(Curr_video)
    working_dir = "/home/gustavo/Cockatiels/VIDEOS/PROCESSING/"
    working_file = Curr_video
    #print(working_file)

    tracker.decode(working_dir, working_file)

    move_command2 = str("mv /home/gustavo/Cockatiels/VIDEOS/PROCESSING/" + Curr_video + str(".MP4 /home/gustavo/Cockatiels/VIDEOS/DONE/"))
    terminal(move_command2)
    move_command3 = str("mv /home/gustavo/Cockatiels/VIDEOS/PROCESSING/" + Curr_video + str("_output.mp4 /home/gustavo/Cockatiels/VIDEOS/OUTPUTS/"))
    terminal(move_command3)
    count_files = terminal(str("ls Cockatiels/VIDEOS/TO_PROCESS/ | wc -l" ))




###Copy of script
###!/bin/bash/
##import barcode_tracker_cockatiels2 as tracker
##import cv2 
##import numpy as np
##import matplotlib.pyplot as plt
##import pandas as pd
##import datetime as dt
##from scipy.spatial import distance as dist
##
##from pinpoint import TagDictionary as TagList
##import glob
##import os
##import pickle
##import subprocess
###%matplotlib inline
####get_ipython().magic(u'matplotlib inline')
####cv2.setNumThreads(0) # Turn off multithreading to prevent errors
####print "packages loaded"cock
##
##def terminal(line):
##    command = subprocess.Popen([line], stdout=subprocess.PIPE, shell=True)
##    return command.stdout.read()
##
##
##abc1 = str("ls " + "COCKATIELS/VIDEOS/TO_PROCESS/" + " | head --lines=1")
##Curr_video1 = terminal(abc1)
###print(Curr_video1)
##Curr_video = Curr_video1[:-5]
##
##move_command = str("mv /home/gustavo/COCKATIELS/VIDEOS/TO_PROCESS/" + Curr_video + ".MP4 /home/gustavo/COCKATIELS/VIDEOS/PROCESSING/")
###print(move_command)
##terminal(move_command)
##
##print(Curr_video)
###print(Curr_video)
##working_dir = "/home/gustavo/COCKATIELS/VIDEOS/PROCESSING/"
##working_file = Curr_video
###print(working_file)
##
##tracker.decode(working_dir, working_file)
##
##move_command2 = str("mv /home/gustavo/COCKATIELS/VIDEOS/PROCESSING/" + Curr_video + str(".MP4 /home/gustavo/COCKATIELS/VIDEOS/DONE/"))
##terminal(move_command2)
