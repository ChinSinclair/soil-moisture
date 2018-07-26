import RPi.GPIO as GPIO
import time 
import csv

# GPIO 21 is used in this case
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# initialise string output to empty string
output = “”

# filename is temp.csv in CSV format
csvfile = “temp.csv”

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500)

while True:
    # read data ever 1 second
	time.sleep(1)
	if GPIO.input(channel):
		output = “Moisture: No water detected”
	else:
		output =”Moisture: Water detected”

    # print string output upon execution
	print(output)

    # open file to write string output, still have bugs where characters are being stored in columns separately
	with open(csvfile, “a”) as output1:
		write = csv.writer(output1)
		writer.writerow(output) 
