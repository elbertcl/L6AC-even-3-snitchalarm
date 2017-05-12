import bluetooth
import time
import RPi.GPIO as GPIO
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

fromaddr = "noreply.snitchalarm@gmail.com"
toaddr = "jeremy.jodi168@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Door has been opened"

body = "Not You? Contact your neighbours or the local security."
msg.attach(MIMEText(body, 'plain'))

name ="Snitch"
open = 0
print("Hello " + name)

while True:

	result = bluetooth.lookup_name('80:EA:96:E0:43:D5', timeout = 5)
	if (result != None) :
		print "Your phone is on the perimeter"
	else :
		print "Your phone is not on the perimeter"
		if GPIO.input(18):
			if open == 0:
				print("Door is open")
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				print("ok")
				server.login(fromaddr, "magnet123")
				print("2")
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()
				open = 1
		if GPIO.input(18) == False:
			if open == 1:
				print("Door is closed")
				open = 0

	
		
