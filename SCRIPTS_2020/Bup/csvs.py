import csv
import cv2
import os
with open("/home/gustavo/COCKATIELS/CSV/Feeder_C2_2018-07-26.csv", "rb") as data_file:
    reader = csv.reader(data_file,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    print(str("Photos = ") + str(row_count))

list = os.listdir(dir) # dir is your directory path
number_files = len(list)
print number_files

cap = cv2.VideoCapture("/home/gustavo/COCKATIELS/VIDEOS/OUTPUTS/Feeder_C2_2018-07-26_output.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frames = ' + str(length))

if length != row_count:
    print ('ERROR check ffmpeg')

    
