import urllib.request
import shutil
import os
from time import sleep  # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO # Allows us to call our GPIO pins and names it just GPIO
 
GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 23           # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
OUTPUT_PIN = 18
GPIO.setup(INPUT_PIN, GPIO.IN)  # Set our input pin to be an input
GPIO.setup(OUTPUT_PIN, GPIO.OUT)

processingDone=0
USBavalable=0
def statusUSB(channel):
    USBavailable=1

GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, callback=statusUSB, bouncetime=200) # Wait for the input to go low, run the function when it does


print('Beginning file download with urllib2...')

url = 'https://arweave.net/HQ-GUuX8Lk4rG6NXg8GKtCPAol4lCOyazn7c4OM-gfw'
urllib.request.urlretrieve(url, '/home/pi/GXP2/Videos/video.mp4')

target_dir = '/home/pi/GXP2/processing'
source_dir = '/home/pi/GXP2/Videos'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

##Code for HD player###############################

    #To be written......
    processingDone=1
###################################################

while(processingDone):
    if(USBavailable):
        #switchUSB
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
        sleep(1)
        
        #copy files to HDplayer folder
        source_dir = '/home/pi/GXP2/processing'
        target_dir = '/home/pi/GXP2/HDPlayerUsbExport' ##To be edited for USBdirectory
    
        file_names = os.listdir(source_dir)
    
        for file_name in file_names:
            shutil.move(os.path.join(source_dir, file_name), target_dir)
        
        #switchBackUSB
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
        sleep(1)
        processingDone=0
        USBavailable=0
    sleep(1);
    
