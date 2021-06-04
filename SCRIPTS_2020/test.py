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
ip = (str(ip_pi[1]))[3:]
print(ip)



##with open('/home/gustavo/COCKATIELS/REPORTS/texto') as report:
##    readCSV = csv.reader(report)
##    print(readCSV)
##    message = report.append("/home/gustavo/COCKATIELS/REPORTS/texto") + str("mensaje 1")
##    texto = (str("echo \"" + message + "\" > /home/gustavo/COCKATIELS/REPORTS/texto"))
##    terminal(texto)
##    #ip_pi = []
##    pi_name = []
##    for row in readCSV:
##        ips = row[1]
##        names = row[0]
##
##        pi_name.append(names)
##        ip_pi.append(ips)
