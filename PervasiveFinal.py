# Importing necessary libraries
import bluetooth # Used for phone detection
import time # Used for sleep function
import RPi.GPIO as GPIO # Necessary for Raspberry PI GPIO

# Used for emails
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Setting the GPIO Mode to BCM
GPIO.setmode(GPIO.BCM)
# Setting up the connection for BCM number 18
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The Snitch Alarm's service email that is going to send the notification (email)
fromaddr = "noreply.snitchalarm@gmail.com"
# The user's email
toaddr = "jeremy.jodi168@gmail.com"

# Setting the email's information (sender and receiver's email address, along with the email's subject and message)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Door has been opened"

body = "Not You? Contact your neighbours or the local security."
msg.attach(MIMEText(body, 'plain'))

# Initial console message of the program running (all console messages will not be shown to the user)
name ="User"
print("Hello, " + name)

# Initializing the door as closed
open = 0

while True:
	# Getting the user's phone's bluetooth connectivity (from the device's bluetooth MAC address)
	result = bluetooth.lookup_name('80:EA:96:E0:43:D5', timeout = 5)
	# If the bluetooth connectivity is found, the system will enter safe mode
	if (result != None) :
		print "Your phone is on the perimeter"
	# If the bluetooth connectivity is NOT found, the system will wait for a door breach
		print "Your phone is not on the perimeter"
		# If the program detects the door being opened, send the notification email to the user
		if GPIO.input(18):
			if open == 0:
				print("Door is open")
				# Email sending is using the Gmail's SMTP service
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				print("Authenticating to server...")
				# Authenticating to Gmail by logging in to the Snitch Alarm's email
				server.login(fromaddr, "magnet123")
				print("Authentication completed")
				text = msg.as_string()
				# Sending the email
				server.sendmail(fromaddr, toaddr, text)
				server.quit()
				# Mark the door as opened, such that the program will not be sending multiple emails for the notification
				open = 1
		# If the program detects the door being closed ...
		if GPIO.input(18) == False:
			if open == 1:
				print("Door is closed")
				# Mark the door as closed
				open = 0

	
		
