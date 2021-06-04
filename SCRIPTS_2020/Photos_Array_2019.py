import time
import picamera
from datetime import datetime
import os
from PIL import Image, ImageDraw, ImageFont
import csv

pi_name = "Feeder_C2"


def photos(): # takes photos between 7am and 5pm
    if hours >= 5 and hours <= 6:
        every_10('night', (9200)) ##darker
    else:
        if hours >= 7 and hours <= 8:
            every_10('auto', (2400)) ##not too dark
        else:
            if hours >= 9 and hours <= 17:
                every_10('snow', (1400)) ##normal bright conditions
            else :
		print ("too dark for photos")
                os.system(str('sudo reboot'))

    
        
def every_10(exp_mode, speed):
    
    with picamera.PiCamera() as camera:
        camera.rotation = 0
        camera.resolution = (1900,1200)
        camera.exposure_mode = exp_mode
        camera.brightness = 50
        camera.shutter_speed = speed
        #camera.exposure_compensation = -7
        camera.color_effects = (128, 128)
        camera.contrast = (25)
        camera.sharpness = (25)
        camera.ISO = (0)
        time.sleep(0)

        timest = (pi_name + '_{:%Y-%m-%d}'.format(datetime.now()))
        timeofframe = ('{:%Y-%m-%d_%H%M%S}'.format(datetime.now()))
        if not os.path.exists(str('/home/pi/APAPORIS/PHOTOS/' + timest)):
            os.makedirs(str('/home/pi/APAPORIS/PHOTOS/' + timest))

        ilist = os.listdir(str('/home/pi/APAPORIS/PHOTOS/' + timest))
        i = len(ilist)
        print (i)

        filename = str(timest + str('_') + str("%05d" % i) + '.jpg')
        camera.annotate_text= str(timeofframe + "-" + filename) 
          
        camera.capture(str('/home/pi/APAPORIS/PHOTOS/' + timest + str('/') + filename))
        line = str(timeofframe + ", " + filename)
        print(line)
        f= open('/home/pi/APAPORIS/CSV/' + timest + '.csv', "a+")
        f.write(line + "\n")
        f.close()

        time.sleep(0) # wait 1 sec
        
        
while 1==1: #every 10 min
    hours = int(('{:%H}'.format(datetime.now())))
    
    print (hours)
    photos()
