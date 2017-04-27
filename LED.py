import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for i in range(0, 2):
	GPIO.setup(18,GPIO.OUT)
	GPIO.setup(23,GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	print "RED on"
	GPIO.output(18,GPIO.HIGH)
	time.sleep(3)
	print "YELLOW on"
	GPIO.output(23,GPIO.HIGH)
	time.sleep(1)
	print "RED YELLOW off"
	GPIO.output (18, GPIO.LOW)
	GPIO.output (23, GPIO.LOW)
	
	print "GREEN on"
	GPIO.output (24, GPIO.HIGH)
	time.sleep(3)
	print "GREEN off YELLOW on"
	GPIO.output(24, GPIO.LOW)
	GPIO.output(23, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(23, GPIO.LOW)
