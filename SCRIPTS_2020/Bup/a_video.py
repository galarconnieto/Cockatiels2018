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
##a_video = str('ffmpeg -r 24 -i /home/gustavo/COCKATIELS/PHOTOS/Cockatiels_2018-06-16/Cockatiels_2018-06-16_%05d.jpg Cockatiels_2018-06-16.MP4')
##terminal(a_video)
target_folder = str('New')

remove_command = str('ssh ' + ip_pi + ' rm -rf' + ' COCKATIELS/MOVED/' + target_folder + '/')
terminal(remove_command)
