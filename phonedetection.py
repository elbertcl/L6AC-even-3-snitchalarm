import bluetooth
import time

while True:
	result = bluetooth.lookup_name('80:EA:96:E0:43:D5', timeout = 5)
	if (result != None) :
		print "Your phone is on the perimeter"
	else :
		print "Your phone is not on the perimeter"

	time.sleep(10)
