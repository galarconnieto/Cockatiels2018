# Copy folder
scp -r pi@10.76.0.91:COCKATIELS/PHOTOS/Cockatiels_2018-06-13 /home/gustavo/COCKATIELS/Cockatiels_2018-06-13

# Remotelly connect to pi
ssh pi:ip.address

###ON THE PI

# Measure temperature

/opt/vc/bin/vcgencmd measure_temp

# Count number of files in folder
ls COCKATIELS/PHOTOS/Cockatiels_2018-06-23 | wc -l

# Remove folder
rm -rf Cockatiels_2018-06-12/


#Check number of python processes
ps -A | grep python


# Take photos
python /home/pi/COCKATIELS/SCRIPTS/Photos_Outdoors2.py


# Photo to video
ffmpeg -r 24 image2 -i file_name_%05d.jpg file_name.MP4


#ssh keygen copy to pi
ssh-copy-id -i ~/.ssh/tatu-key-ecdsa pi@10.76.0.91


## Copy the last photo ### Change folder and file name
scp pi@10.76.0.92:/home/pi/COCKATIELS/PHOTOS/Feeder_C2_2018-07-20/Feeder_C2_2018-07-20_01822.jpg /home/gustavo/COCKATIELS/

##Show last photo

python /home/gustavo/COCKATIELS/Show_photo.py


